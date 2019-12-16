# -*- coding: utf-8 -*-

class BaseRepository:

    
    def merge_branch(self, source, target):
        raise NotImplementedError()
    

    def is_exist_branch(self, name):
        raise NotImplementedError()



