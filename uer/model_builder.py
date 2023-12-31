# -*- encoding:utf-8 -*-
import torch
from uer.layers.embeddings import BertEmbedding
from uer.layers.relevance_score_embedding import RelevanceScoreEmbedding
from uer.encoders.bert_encoder import BertEncoder
from uer.encoders.relevance_score_encoder import RelevanceEncoder
from uer.encoders.rnn_encoder import LstmEncoder, GruEncoder
from uer.encoders.birnn_encoder import BilstmEncoder
from uer.encoders.cnn_encoder import CnnEncoder, GatedcnnEncoder
from uer.encoders.attn_encoder import AttnEncoder
from uer.encoders.gpt_encoder import GptEncoder
from uer.encoders.mixed_encoder import RcnnEncoder, CrnnEncoder
from uer.targets.bert_target import BertTarget
from uer.targets.lm_target import LmTarget
from uer.targets.cls_target import ClsTarget
from uer.targets.mlm_target import WordMlmTarget, RelMlmTarget, EntMlmTarget
from uer.targets.nsp_target import NspTarget
from uer.targets.s2s_target import S2sTarget
from uer.targets.bilm_target import BilmTarget
from uer.subencoders.avg_subencoder import AvgSubencoder
from uer.subencoders.rnn_subencoder import LstmSubencoder
from uer.subencoders.cnn_subencoder import CnnSubencoder
from uer.models.model import Model
from uer.models.relevance_score_model import RelevanceScoreModel


def build_model(args):
    """
    Build universial encoder representations models.
    The combinations of different embedding, encoder, 
    and target layers yield pretrained models of different 
    properties. 
    We could select suitable one for downstream tasks.
    """

    if args.subword_type != "none":
        subencoder = globals()[args.subencoder.capitalize() + "Subencoder"](args, len(args.sub_vocab))
    else:
        subencoder = None

    embedding = BertEmbedding(args, len(args.vocab))
    mask_embedding = BertEmbedding(args, len(args.vocab))
    relevance_embedding = RelevanceScoreEmbedding(args, len(args.vocab))
    encoder = globals()[args.encoder.capitalize() + "Encoder"](args)
    mask_encoder = globals()[args.encoder.capitalize() + "Encoder"](args)
    relevance_encoder = globals()[args.relevance_encoder.capitalize() + "Encoder"](args)
    target = globals()[args.target.capitalize() + "Target"](args, len(args.vocab))
    model = Model(args, embedding, encoder, target, subencoder)
    mask_model = Model(args, mask_embedding, mask_encoder, target, subencoder)
    relevance_model = RelevanceScoreModel(args, relevance_embedding, relevance_encoder)

    return model, mask_model, relevance_model
