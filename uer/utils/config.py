# -*- encoding:utf-8 -*-
import json
import codecs

def load_hyperparam(args):
    with codecs.open(args.config_path, "r", "utf-8") as f:
        param = json.load(f)
    args.emb_size = param.get("emb_size", 768)
    args.hidden_size = param.get("hidden_size", 768)
    args.kernel_size = param.get("kernel_size", 3)
    args.block_size = param.get("block_size", 2)
    args.feedforward_size = param.get("feedforward_size", None)
    args.heads_num = param.get("heads_num", None)
    args.layers_num = param.get("layers_num", 12)
    args.adapter_size = param.get("adapter_size", 64)
    args.dropout = param.get("dropout", 0.1)
    args.down_and_up_projection_size = param.get("down_and_up_projection_size", None)
    args.KIA_layer_num = param.get("KIA_layer_num", None)
    return args