# ============================================================================
# FILE: sorter/oldfiles.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

import math

from denite.base.filter import Base
from denite.util import Nvim, UserContext, Candidates


class Filter(Base):

    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'sorter/oldfiles'
        self.description = 'sort candidates by v:oldfiles'

    def on_init(self, context: UserContext) -> None:
        # rviminfo! is broken in Vim8
        if self.vim.call('has', 'nvim'):
            self.vim.command('wviminfo | rviminfo!')

    def filter(self, context: UserContext) -> Candidates:
        oldfiles = {x: i for i, x in enumerate(self.vim.vvars['oldfiles'])}
        return sorted(context['candidates'],
                      key=lambda x: x.get(x['action__path'], math.inf))
