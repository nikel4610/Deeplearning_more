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