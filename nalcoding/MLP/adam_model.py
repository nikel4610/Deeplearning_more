import mlp_model

class AdamModel(mlp_model.MLPModel):
    def __init__ (self, name, dataset, hconfigs):
        self.use_adam = False # 메서드 호출 전에 True로 변경
        super(AdamModel, self).__init__(name, dataset, hconfigs)
