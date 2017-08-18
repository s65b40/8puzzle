# -*- coding:utf-8 -*-
class puzzle:
    def __init__(self, seq, goalseq):
        self.iniseq = seq
        self.tmpseq = seq
        self.goalseq = goalseq
        self.cp_list = []
        self.cp_list.append(self.iniseq)
        self.tier = []
        self.tier.append([self.iniseq])
        print self.tier
        # print self.stre_u(seq)

        # self.bfs_search(self.cp_list, self.tier)
        self.dfs_searcht(self.iniseq, self.goalseq)

    def bfs_search(self, cplist, tier):
        flag = 0
        while (1):
            tier.append([])
            for i in range(0, len(tier[flag])):
                if tier[flag][i] != 'null':  # judge if the sequence is null
                    self.bfs_stretch(tier[flag][i], tier[flag + 1])
                else:
                    tier[flag + 1].append('null')
                    tier[flag + 1].append('null')
                    tier[flag + 1].append('null')
                    tier[flag + 1].append('null')
            print tier
            flag += 1

    def dfs_search(self):

        # initialize graph
        times = 5
        flag = 1
        dfs_stack = []
        while (times):
            self.tier.append([])
            for i in range(0, 4 ** flag):
                self.tier[flag].append('e')
            flag += 1
            times -= 1
        # print tier
        self.cplist.append(self.iniseq)
        # dfs_stack.append((0,0))
        flag_tier = 0
        flag_pos = 0
        while (1):
            if self.tier[flag_tier + 1][flag_pos * 4] == 'e':
                dfs_stack.append((flag_tier + 1, flag_pos * 4))
            if self.tier[flag_tier + 1][flag_pos * 4 + 1] == 'e':
                dfs_stack.append((flag_tier + 1, flag_pos * 4 + 1))

    def dfs_searcht(self, seq, goalseq):
        count = 0
        iniseq = seq
        tseq = seq
        dfs_stack = []
        dfs_stack.append(tseq)
        cplst = []
        while (1):
            while (1):
                if tseq[0] != '0' and tseq[1] != '0' and tseq[2] != '0':
                    utseq = self.stre_u(tseq)
                    if utseq == goalseq:
                        print 'find the goal dfs'
                        print count
                        exit(0)
                    if utseq not in cplst:
                        dfs_stack.append(utseq)
                        count += 1
                        cplst.append(utseq)
                        tseq = utseq
                        continue
                    else:
                        pass
                if tseq[6] != '0' and tseq[7] != '0' and tseq[8] != '0':
                    dtseq = self.stre_d(tseq)
                    if dtseq == goalseq:
                        print 'find the goal dfs'
                        print count
                        exit(0)
                    if dtseq not in cplst:
                        dfs_stack.append(dtseq)
                        count += 1
                        cplst.append(dtseq)
                        tseq = dtseq
                        continue
                    else:
                        pass
                if tseq[0] != '0' and tseq[3] != '0' and tseq[6] != '0':
                    ltseq = self.stre_l(tseq)
                    if ltseq == goalseq:
                        print 'find the goal dfs'
                        print count
                        exit(0)
                    if ltseq not in cplst:
                        dfs_stack.append(ltseq)
                        count += 1
                        cplst.append(ltseq)
                        tseq = ltseq
                        continue
                    else:
                        pass
                if tseq[2] != '0' and tseq[5] != '0' and tseq[8] != '0':
                    rtseq = self.stre_r(tseq)
                    if rtseq == goalseq:
                        print 'find the goal dfs'
                        print count
                        exit(0)
                    if rtseq not in cplst:
                        dfs_stack.append(rtseq)
                        count += 1
                        cplst.append(rtseq)
                        tseq = rtseq
                        continue
                    else:
                        pass
                dfs_stack = dfs_stack[:-1]
                tseq = dfs_stack[-1]

    def bfs_stretch(self, tseq, tlist):
        '''
        :param tseq: present sequence of puzzle
        :param tlist: present list that stores
        :return:
        '''
        # with an order of up, down, left, right
        # up
        if tseq[0] != '0' and tseq[1] != '0' and tseq[2] != '0':
            utp = self.stre_u(tseq)
            if utp not in self.cp_list:
                tlist.append(utp)
                self.cp_list.append(utp)
            else:
                tlist.append('null')
        else:
            tlist.append('null')

        # down
        if tseq[6] != '0' and tseq[7] != '0' and tseq[8] != '0':
            dtp = self.stre_d(tseq)
            if dtp not in self.cp_list:
                tlist.append(dtp)
                self.cp_list.append(dtp)
            else:
                tlist.append('null')
        else:
            tlist.append('null')

        # left
        if tseq[0] != '0' and tseq[3] != '0' and tseq[6] != '0':
            ltp = self.stre_l(tseq)
            if ltp not in self.cp_list:
                tlist.append(ltp)
                self.cp_list.append(ltp)
            else:
                tlist.append('null')
        else:
            tlist.append('null')

        # right
        if tseq[2] != '0' and tseq[5] != '0' and tseq[8] != '0':
            rtp = self.stre_r(tseq)
            if rtp not in self.cp_list:
                tlist.append(rtp)
                self.cp_list.append(rtp)
            else:
                tlist.append('null')
        else:
            tlist.append('null')

        if self.goalseq in tlist:
            print 'find the goal'
            self.output(tlist.index(self.goalseq))
            return

    def output(self, pos):
        outlst = []
        dirlst = []
        print 'It has searched for %d time(s)' % (len(self.tier) - 1)
        for k in range(len(self.tier) - 1, -1, -1):
            outlst.append(self.tier[k][pos])
            dirlst.append(pos % 4)

            # print self.tier[k][pos]
            pos /= 4
        # print  outlst, dirlst
        dirlst = dirlst[:-1]
        for l in range(len(dirlst) - 1, -1, -1):
            print outlst[l + 1]
            if dirlst[l] == 0:
                print 'up'
            elif dirlst[l] == 1:
                print 'down'
            elif dirlst[l] == 2:
                print 'left'
            else:
                print 'right'
        print outlst[0]
        exit(0)

    def stre_u(self, tseq):
        # find where the blank is
        pos = tseq.index('0')
        # destination
        dpos = pos - 3
        newstr = tseq[0:dpos] + tseq[pos] + tseq[dpos + 1:pos] + tseq[dpos] + tseq[pos + 1:]
        return newstr

    def stre_d(self, tseq):
        pos = tseq.index('0')
        dpos = pos + 3
        newstr = tseq[0:pos] + tseq[dpos] + tseq[pos + 1:dpos] + tseq[pos] + tseq[dpos + 1:]
        return newstr

    def stre_l(self, tseq):
        pos = tseq.index('0')
        dpos = pos - 1
        newstr = tseq[0:dpos] + tseq[pos] + tseq[dpos] + tseq[pos + 1:]
        return newstr

    def stre_r(self, tseq):
        pos = tseq.index('0')
        dpos = pos + 1
        newstr = tseq[0:pos] + tseq[dpos] + tseq[pos] + tseq[dpos + 1:]
        return newstr


# puzzle("134862705","123804765")
puzzle("134862705", "134862705")
