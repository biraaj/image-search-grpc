# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image_search.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12image_search.proto\x12\x0cimage_search\" \n\rSearchRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\"#\n\rImageResponse\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x32V\n\x0bImageSearch\x12G\n\x0bSearchImage\x12\x1b.image_search.SearchRequest\x1a\x1b.image_search.ImageResponseB2Z0github.com/biraaj/image-search-grpc/image_searchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'image_search_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z0github.com/biraaj/image-search-grpc/image_search'
  _globals['_SEARCHREQUEST']._serialized_start=36
  _globals['_SEARCHREQUEST']._serialized_end=68
  _globals['_IMAGERESPONSE']._serialized_start=70
  _globals['_IMAGERESPONSE']._serialized_end=105
  _globals['_IMAGESEARCH']._serialized_start=107
  _globals['_IMAGESEARCH']._serialized_end=193
# @@protoc_insertion_point(module_scope)