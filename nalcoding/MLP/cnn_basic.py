import adam_model
import numpy as np
import math_util

class CnnBasicModel(adam_model.AdamModel):
    def __init__(self, name, dataset, hconfigs, show_maps=False):
        if isinstance(hconfigs, list) and not isinstance(hconfigs[0], (list, int)):
            hconfigs = [hconfigs] # 오류 방지
        self.show_maps = show_maps
        self.need_maps = False
        self.kernels = []
        super(CnnBasicModel, self).__init__(name, dataset, hconfigs)
        self.use_adam = True # adam 플래그의 초깃값을 True로 바꾸어 자동 적용

def get_layer_type(hconfig):
    if not isinstance(hconfig, list):
        return 'full'
    return hconfig[0]

def get_conf_param(hconfig, key, defval = None):
    if not isinstance(hconfig, list):
        return defval
    if len(hconfig) <= 1:
        return defval
    if not key in hconfig[1]:
        return defval
    return hconfig[1][key]

def get_conf_param_2d(val, hconfig, key, defval = None):
    if len(hconfig) <= 1:
        return defval
    if not key in hconfig[1]:
        return defval
    if isinstance(val, list):
        return val
    return [val, val]

def cnn_basic_alloc_layer_param(self, input_shape, hconfig):
    layer_type = get_layer_type(hconfig)

    m_name = 'alloc_{}_layer'.format(layer_type)
    method = getattr(self, m_name)
    pm, output_shape = method(input_shape, hconfig)

    return pm, output_shape

CnnBasicModel.alloc_layer_param = cnn_basic_alloc_layer_param

def cnn_basic_forward_layer(self, x, hconfig, pm):
    layer_type = get_layer_type(hconfig)

    m_name = 'forward_{}_layer'.format(layer_type)
    method = getattr(self, m_name)
    y, aux = method(x, hconfig, pm)

    return y, aux

CnnBasicModel.forward_layer = cnn_basic_forward_layer

def cnn_basic_backprop_lyaer(self, G_y, hconfig, pm, aux):
    layer_type = get_layer_type(hconfig)

    m_name = 'backprop_{}_layer'.format(layer_type)
    method = getattr(self, m_name)
    G_input = method(G_y, hconfig, pm, aux)

    return G_input

CnnBasicModel.backprop_layer = cnn_basic_backprop_lyaer

def cnn_basic_alloc_full_layer(self, input_shape, hconfig):
    input_cnt = np.prod(input_shape)
    output_cnt = get_conf_param(hconfig, 'width', hconfig) # 다차원 형태로 출력 -> [output_cnt] 리스트로 반환

    weight = np.random.normal(0, self.rand_std, [input_cnt, output_cnt])
    bias = np.zeros([output_cnt])

    return {'w':weight, 'b':bias}, [output_cnt] # 리스트로 반환

def cnn_basic_alloc_conv_layer(self, input_shape, hconfig):
    assert len(input_shape) == 3 # 입력 형태가 3차원인지 검사
    xh, xw, xchn = input_shape
    kh, kw = get_conf_param_2d(hconfig, 'ksize')
    ychn = get_conf_param(hconfig, 'chn')

    kernel = np.random.normal(0, self.rand_std, [kh, kw, xchn, ychn])
    bias = np.zeros([ychn])

    if self.show_maps:
        self.kernels.append(kernel)

    return {'k':kernel, 'b':bias}, [xh, xw, ychn]

def cnn_basic_alloc_pool_layer(self, input_shape, hconfig):
    assert len(input_shape) == 3
    xh, xw, xchn = input_shape
    sh, sw = get_conf_param_2d(hconfig, 'stride')

    assert xh % sh == 0
    assert xw % sw == 0

    return {}, [xh // sh, xw // sw, xchn]

CnnBasicModel.alloc_full_layer = cnn_basic_alloc_full_layer
CnnBasicModel.alloc_conv_layer = cnn_basic_alloc_conv_layer
CnnBasicModel.alloc_max_layer = cnn_basic_alloc_pool_layer
CnnBasicModel.alloc_avg_layer = cnn_basic_alloc_pool_layer

def cnn_basic_forward_full_layer(self, x, hconfig, pm):
    if pm is None:
        return x, None

    x_org_shape = x.shape

    if len(x.shape) != 2: # 2차원 행렬이 아닌 경우 차원을 모두 모아서 전처리
        mb_size = x.shape[0]
        x = x.reshape([mb_size, -1])

    affine = np.matmul(x, pm['w']) + pm['b']
    y = self.activate(affine, hconfig) # 비선형 함수 적용

    return y, [x, y, x_org_shape]

CnnBasicModel.forward_full_layer = cnn_basic_forward_full_layer

def cnn_basic_backprop_full_layer(self, G_y, hconfig, pm, aux):
    if pm is None:
        return G_y

    x, y, x_org_shape = aux

    G_affine = self.activate_derv(G_y, y, hconfig)

    g_affine_weight = x.transpose()
    g_affine_input = pm['w'].transpose()

    G_weight = np.matmul(g_affine_weight, G_affine)
    G_bias = np.sum(G_affine, axis=0)
    G_input = np.matmul(G_affine, g_affine_input)

    self.update_param(pm, 'w', G_weight)
    self.update_param(pm, 'b', G_bias)

    return G_input.reshape(x_org_shape)

CnnBasicModel.backprop_full_layer = cnn_basic_backprop_full_layer

def cnn_basic_activate(self, affine, hconfig):
    if hconfig is None:
        return affine

    func = get_conf_param(hconfig, 'actfunc', 'relu')

    if func == 'none':
        return affine
    elif func == 'relu':
        return math_util.relu(affine)
    elif func == 'sigmoid':
        return math_util.sigmoid(affine)
    else:
        assert 0

def cnn_basic_activate_derv(self, G_y, y, hconfig):
    if hconfig is None:
        return G_y

    func = get_conf_param(hconfig, 'actfunc', 'relu')

    if func == 'none':
        return G_y
    elif func == 'relu':
        return math_util.relu_derv(y) * G_y
    elif func == 'sigmoid':
        return math_util.sigmoid_derv(y) * G_y
    else:
        assert 0

CnnBasicModel.activate = cnn_basic_activate
CnnBasicModel.activate_derv = cnn_basic_activate_derv

def forward_conv_layer_adhoc(self, x, hconfig, pm):
    mb_size, xh, xw, xchn = x.shape
    kh, kw, _, ychn = pm['k'].shape

    conv = np.zeros((mb_size, xh, xw, ychn))

    for n in range(mb_size):
        for r in range(xh):
            for c in range(xw):
                for ym in range(ychn):
                    for i in range(kh):
                        for j in range(kw):
                            rx = r + i - (kh-1) // 2
                            cx = c + j - (kw-1) // 2
                            if rx < 0 or rx >= xh:
                                continue
                            if cx < 0 or cx >= xw:
                                continue
                            for xm in range(xchn):
                                kval = pm['k'][i][j][xm][ym]
                                ival = x[n][rx][cx][xm]
                                conv[n][r][c][ym] += kval * ival
    y = self.activate(conv + pm['b'], hconfig)
    return y, [x, y]

def forward_conv_layer_better(self, x, hconfig, pm):
    mb_size, xh, xw, xchn = x.shape
    kh, kw, _, ychn = pm['k'].shape

    conv = np.zeros((mb_size, xh, xw, ychn))

    bh, bw = (kh-1) // 2, (kw-1) // 2
    eh, ew = xh + kh - 1, xw + kw - 1

    x_ext = np.zeros((mb_size, eh, ew, xchn)) # 여기서 추가된 열은 0으로 채워짐
    x_ext[:, bh:bh + xh, bw:bw + xw, :] = x # 버퍼의 중앙 부분에 입력 복사

    # 출력 체널별로 커널의 나머지 세 차원을 한 차원 벡터로 축소
    k_flat = pm['k'].transpose([3, 0, 1, 2]).reshape([ychn, -1])

    for n in range(mb_size):
        for r in range(xh):
            for c in range(xw):
                for ym in range(ychn):
                    xe_flat = x_ext[n, r:r+kh, c:c+kw, :].flatten()
                    conv[n, r, c, ym] = (xe_flat*k_flat[ym]).sum()

    y = self.activate(conv + pm['b'], hconfig)

    return y, [x, y]

def cnn_basic_forward_conv_layer(self, x, hconfig, pm):
    mb_size, xh, xw, xchn = x.shape
    kh, kw, _, ychn = pm['k'].shape

    x_flat = get_ext_regions_for_conv(x, kh, kw)
    k_flat = pm['k'].reshape([kh*kw*xchn, ychn]) # 4차원 텐서를 2차원 행렬로 바꿈
    conv_flat = np.matmul(x_flat, k_flat)
    conv = conv_flat.reshape([mb_size, xh, xw, ychn]) # 2차원 행렬을 4차원 텐서로 바꿈

    y = self.activate(conv + pm['b'], hconfig)

    if self.need_maps: # 시각화 정보 수집
        self.maps.append(y)

    return y, [x_flat, k_flat, x, y]

CnnBasicModel.forward_conv_layer = cnn_basic_forward_conv_layer

def cnn_basic_backprop_conv_layer(self, G_y, hconfig, pm, aux):
    x_flat, k_flat, x, y = aux

zzaa