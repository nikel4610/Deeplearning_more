import adam_model
import numpy as np

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

    if len(x.shape) != 2:
        mb_size = x.shape[0]
        x = x.reshape([mb_size, -1])

    affine = np.matmul(x, pm['w']) + pm['b']
    y = self.activate(affine, hconfig)

    return y, [x, y, x_org_shape]

CnnBasicModel.forward_full_layer = cnn_basic_forward_full_layer