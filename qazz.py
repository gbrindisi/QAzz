#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from github3 import GitHub, login

class QAzz(object):
    """docstring for ClassName"""
    def __init__(self):
        self.gh = GitHub() # login(username,pwd)
        self.repo = self._get_repository('gbrindisi','wordpot')
        self.contributors = []
        self.last_commit = None
        self._get_contributors_statistics()
        

    def _get_repository(self,owner,repository):
        return self.gh.repository(owner,repository)

    def _get_contributors_statistics(self):
        for c in self.repo.iter_contributor_statistics():
            contributor = {
                'name': c.author,
                'total': c.total,
                'last' : None
            }
            for w in reversed(c.alt_weeks):
                if w['commits'] != 0:
                    contributor['last'] = w['start of week']
                    break

            self.contributors.append(contributor)

        # Sort by date
        self.contributors = sorted(self.contributors, key=lambda k: k['last'])

        # Store last commit
        self.last_commit = self.contributors[-1]['last']

    def _print_banner(self):
        print u"""

        
         ██████╗  █████╗ ███████╗███████╗ ..??
        ██╔═══██╗██╔══██╗╚══███╔╝╚══███╔╝
        ██║   ██║███████║  ███╔╝   ███╔╝ 
        ██║▄▄ ██║██╔══██║ ███╔╝   ███╔╝  
        ╚██████╔╝██║  ██║███████╗███████╗
         ╚══▀▀═╝ ╚═╝  ╚═╝╚══════╝╚══════╝
          GitHub Repositories Heuristic 
             Quality Assurance Helper

                  by @gbrindisi

        """

    def go(self):
        self._print_banner()
        print "[*] Created:     %s" % self.repo.created_at
        print "[*] Last Commit: %s" % self.last_commit
        print "[*] Stargazers:  %s" % self.repo.stargazers
        print "[*] Watchers:    %s" % self.repo.watchers
        print "[+] Contributors: "
        for c in self.contributors:
            print " |- %s with %d commits (last: %s)" % (c['name'], c['total'],c['last'])

if __name__ == '__main__':
    qazz = QAzz()
    qazz.go()