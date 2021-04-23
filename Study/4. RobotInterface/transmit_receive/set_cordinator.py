from pop import xnode

xnode.atcmd('NI', 'Coordinator')
xnode.atcmd('CE', 0x01)
xnode.atcmd('ID', 0x09)
xnode.atcmd('WR') # 현재 세팅 값 유지 (전원 껐다 켜도 유지)
