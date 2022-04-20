import adam_model

class CnnBasicModel(adam_model.AdamModel):
    def __init__(self, name, dataset, hconfigs, show_maps=False):
        if isinstance(hconfigs, list) and not isinstance(hconfigs[0], (list, int)):
            hconfigs = [hconfigs] # 오류 방지
        self.show_maps = show_maps
        self.need_maps = False
        self.kernals = []
        super(CnnBasicModel, self).__init__(name, dataset, hconfigs)
        self.use_adam = True # adam 플래그의 초깃값을 True로 바꾸어 자동 적용

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

