def count_letters(x):
    return {
        l: x.count(l) for l in set(x)
    }


def day2_1(inp):
    inp = [x.strip() for x in inp.strip().splitlines() if x.strip()]
    two = []
    three = []
    for x in inp:
        count = count_letters(x)
        if 2 in count.values():
            two.append(x)
        if 3 in count.values():
            three.append(x)
    return len(two) * len(three)


def str_dist(a, b):
    dist = 0
    match = []
    for i in range(len(a)):
        if a[i] != b[i]:
            dist += 1
        else:
            match.append(a[i])
    return dist, match


def day2_2(inp):
    inp = [x.strip() for x in inp.strip().splitlines() if x.strip()]
    short_dist = None
    short_match = None
    match_a = None
    match_b = None
    for a in inp:
        for b in inp:
            print(a, b)
            if a == b:
                continue
            dist, match = str_dist(a, b)
            if short_dist is None or dist < short_dist:
                short_dist = dist
                short_match = match
                match_a = a
                match_b = b
    return short_dist, ''.join(short_match), match_a, match_b


inp = """
prtkqyluibmtcwqaezjmhgfndx
prtkqylusbsmcwvaezjmhgfndt
prgkqyluibsocwvamzjmhgkndx
prjkqyluibsocwvahzjmhgfnsx
prtkqylcibsocwvzezjohgfndx
prtkqyluiksocwziezjmhgfndx
prikqyluiksocwvaezjmkgfndx
prtkgyluibsocwvwezjehgfndx
prtkqyluiysocwvaezjghxfndx
prtkqwluibsoxwvaezjmhgfhdx
prtkqylgibsocwvabzjmhzfndx
prtknyltibnocwvaezjmhgfndx
prdkqyluibrocwvaezjmhgnndx
prtwqyluibsoctvcezjmhgfndx
mrtkqyluibgocwvakzjmhgfndx
prtkqaouibsocwvaezjmhwfndx
prtkqyluihjocwvaezjmhgfpdx
prtkqyluikfxcwvaezjmhgfndx
prtkqybuixsocwvaczjmhgfndx
pvtkayluibsocwxaezjmhgfndx
grtkqgluibsocdvaezjmhgfndx
prlkqyluibsochvaezjmhgzndx
prtkqylxibsocmvaezjmhgfkdx
prtkqyluibsqctvaezjmpgfndx
putkqyluibsocqvaezjmhgfndw
prtjqyluibsiclvaezjmhgfndx
prtkqylvpvsocwvaezjmhgfndx
prnkqyluibsocwvaezjmhefsdx
prtktyluibsocwvaezjkhgrndx
prtkqyluibcovwvaezjthgfndx
prtkqcluibiocwvaezjmhggndx
prtkqyluihsocwveezjmhgfydx
prtklyluibsocwqaszjmhgfndx
prtkqyluibsocwvaezjmfznndx
prtkjyluijsocwvaeejmhgfndx
prtkqtluibsonwvaexjmhgfndx
prtkqyluinsocwbaezjmjgfndx
prtkqyluibslckvaezjmhgyndx
prtkqyluibsodwlpezjmhgfndx
prtkquluibsfcwvaezjhhgfndx
prtkqyluhbsocweaezsmhgfndx
prrkqyluinsocxvaezjmhgfndx
prtkqyluibsoswvaezjmhgyqdx
prtkqbluibdocwvlezjmhgfndx
prtkqyfuibsocpvaezjmhgfnwx
prtkqlluibsqjwvaezjmhgfndx
prtkqyluibrocwvaehjmjgfndx
prtkqyluibsoowvaezgmhgendx
wrtjqyluibsocwvaezfmhgfndx
prtvqyluhbsocwvaezjmtgfndx
prtkqyllibspcwvaezjmkgfndx
pqtzqyeuibsocwvaezjmhgfndx
prtkqyluibsolpvaezjmegfndx
przkayguibsocwvaezjmhgfndx
prtkqyluidsocwvaezjmyufndx
prtuqyluibsocwvaezjmfgfnkx
prtkqwluibsrcwvaezjchgfndx
prtkqyluibsotwhaozjmhgfndx
erwkqylhibsocwvaezjmhgfndx
prtkqyluibsocwvgezjmkgfedx
prskqyluiesocwvaezjmggfndx
prtkqylmitsocwvaezjmhgfnox
prtkqyluinnocwvaezjmhgfkdx
prtktyluibsokwvaezjmhgfcdx
prtkqyluibsomwvakvjmhgfndx
prtkqyltibloawvaezjmhgfndx
prtkqyluibxocwvaezgmhgqndx
prtkqyluibskcmvaezjmhgfngx
artkqylubbsotwvaezjmhgfndx
prtkqyluibzocwvhezjmhgfnbx
prskqkluibsocwvaezjmhgfjdx
prtkqyluibwocwvaezjkhglndx
prukqyluissocwvzezjmhgfndx
puhkqyluibsocwvaezjmhgfsdx
qrtkqyluibsocwvaeujmhgfndd
prtkqyluibsoctvaezjmagfnda
prtkquluibsocwkaezjmhgfqdx
prtkqyluubswcwvaezjmhvfndx
prfkqyluibsocwvaemrmhgfndx
pmtkqyluibpocwvaezjmhggndx
prtkqvluibiocwvaezjqhgfndx
prtkgypuibsocwvaezcmhgfndx
prtpqyquibsovwvaezjmhgfndx
prtwqyluiasocwvaexjmhgfndx
mrtzqyluibbocwvaezjmhgfndx
prtkqyluibsocwmaegwmhgfndx
prtkqyluibvncwvaqzjmhgfndx
prtkqyluiusocwvaezjmhmfbgx
prtkqyljibvocwvaezjehgfndx
prtkqyloibsopavaezjmhgfndx
prckqyakibsocwvaezjmhgfndx
prtkqyluibsdcwvaezjmngfddx
prekqylupbsocwvaezemhgfndx
hrtkqyluibhocwvaezjmhgfnde
prmkqyluibsocwvaezzfhgfndx
prtkqyluiccfcwvaezjmhgfndx
pdtkqyluxbsocwvaezjmhgendx
prokqyluibsocwvuezjmsgfndx
prtkqyluibsacwvaezjyhgfndv
prtkqmluibsocavaezjmhgfndc
prtkqyluibsocwvmezjmhgtnqx
prtkqytuibiocyvaezjmhgfndx
pktkqyiuibsocwvwezjmhgfndx
grtrqyluibsocwvaezjmhgfbdx
prtkqylsibjocwvaezjmhgfnyx
prtkqyhutbsocwvaexjmhgfndx
prtknyluibsocmvaezumhgfndx
prtkwyluibsocwvahzjmhgpndx
prtkqywuibsolhvaezjmhgfndx
prtkcyluibsoccvaezjthgfndx
prtkqyrdibsocwvaezjbhgfndx
prtkqyhuqbsocwvaezjmhgfxdx
pytkqyluibsocwvagzjmhgfndv
prtkqyliibsocwvaexwmhgfndx
prtkqyluibshcwvaeljphgfndx
prtkqyluibsocwvaerjzhbfndx
prtkqyduibsocwvaezvmhgfnzx
drtkqylhibsocwvaezjmhmfndx
prtkqyluibsocwvaezamfvfndx
brtkqyluqbsocwvaezjmhgpndx
prtkqyiuibsocwvuezjmhgfngx
urtkqyluibsocqvaeljmhgfndx
prtkqyluikaocwvaezjmhgfjdx
prqkqzouibsocwvaezjmhgfndx
prtkqyluibsocxvaezjmhgfnxv
prlkqyluibsoxwvaeijmhgfndx
prthuyluibsocwvaezjmhgfnhx
potkqyluizsocwvaezjmhifndx
fstkqyduibsocwvaezjmhgfndx
prtkqxluibsocwvaezjmhgffdm
prtkqylpibsozwvaezmmhgfndx
prxkqylbibsocwvaezjphgfndx
srtkqyluibsicnvaezjmhgfndx
prtktyluibsocwvaezjvhgfnax
pctkqyluxbsocwvaezwmhgfndx
prtkqylusbsoclvaezsmhgfndx
pwtkqyluibsocrvaezjmggfndx
prtkqyluibswcwraezjmhgfndd
prtkqyluibtocwiaezjmhgfnax
prtuqyluibsocwvajzjmngfndx
pwtkqyluibsocwvaerjmogfndx
petkqexuibsocwvaezjmhgfndx
pztkqyluibsocwvaerqmhgfndx
prtkqyluobsocwvaezjmapfndx
prtkqyluiinocwvaeljmhgfndx
prtkqyluibsoowvxezjmhgfnnx
lrtkqyluibsocwvfezjmhgfndc
prtkqyluibokcwvahzjmhgfndx
prtkqmlufbsocwvaegjmhgfndx
prtkqylribsocwvanzjmhgfnda
prtkqyluibspxwvaezkmhgfndx
prtiqyluibsbcwvaezjmhgfntx
prikqzluinsocwvaezjmhgfndx
prtkqnldibsocwvaezjmhxfndx
prtkqyluixsocsvaezjmhwfndx
hrtkqyluibsocwvaezjhhgfodx
prtkqyluibsrcwvaezjmhpfwdx
prtkqyluibsocwyaezjmhgffdk
prtkqyluidsocwvalmjmhgfndx
prukquluabsocwvaezjmhgfndx
prckqyluinsmcwvaezjmhgfndx
prbkqymuibsocwvaezjmhgfndc
prtkfylaibsocwvaezjmkgfndx
zrtkqyluibsocwvrbzjmhgfndx
crtkqyluibsocwvaejjmkgfndx
prttqyluibsocyvaezymhgfndx
prtkqylugbsocwvaezjxhgfmdx
prtkqyluibsocwdlezjmhgfnbx
prtkqjluibsocwvaozjhhgfndx
prtcjyluibsocwbaezjmhgfndx
rrtkqyluiblocwvaezjmhgundx
prtkkyluibsocwfaezjmhgfnyx
prtkqyuuibsocwvaezjmhgfogx
prtkyyluvbsocwvaezjmhgfnox
prpkqyluibyocwvaezjmhggndx
pdtkqyluibdocwvaezjmhgfndy
prtklysuibsocwvaezjmhgfnwx
prtkqyluabsouwvaekjmhgfndx
phtkqyluibsocwvaezjmhgfnxt
prtkqyxuibsocwvaezjmhpfnqx
prtkqyluibsodwsaezdmhgfndx
prtkbyluibsohwvaezjmhgfndr
xrtkqylhibsocwvtezjmhgfndx
prtkqyluvysocwvaezbmhgfndx
prtkqieuibsocwvaeojmhgfndx
pctkqyluibsocwvanzjmhgfnux
vrtkqyluibsozwvaezjmhgandx
prtkqyluiusocwvaezjmhmfngx
prbkqyluibsockvaxzjmhgfndx
prtkqyluibsonwvaczjmhgfndi
prtkqyluiblocwvaezjmhgfnau
prtkqyluibsocwvafzuchgfndx
prdkqyluiysocwvaezjmhgfnax
prnkqyouibsocwvaezjmhgfndq
mrtkqgluibsocwvpezjmhgfndx
pvtkqyluibsocwvaczjmhgnndx
trtkqwluibsohwvaezjmhgfndx
prmkqyluibsofwvaezjmhgfrdx
prtyqyluibpdcwvaezjmhgfndx
ertkqylulbsocwvaezjmhgfnax
prtkqyluibsacwvaeijmhgfndf
prtkqyluibyocwvapzjmhgpndx
potkqyluibgocwvaezjmhzfndx
prtkqyluibsocwyaezxmhgfnpx
prtkqkjuibsncwvaezjmhgfndx
prtqqyluibsocwlaezjmhgkndx
prtkxyluibnocwvaezjmhgkndx
prtkqyluiosocwvapzjmxgfndx
prtkqylumbsocwvyezimhgfndx
prukqyluibsocwvyezjmhgindx
prtkqylbibstcwvaezjxhgfndx
pctkqyuuibsocwvaezjuhgfndx
vrtkqyluibsocwvaezjmhgfnll
urtkqyluibsopwvaezjphgfndx
prtkceluibsocwvaepjmhgfndx
prwkxyluibsocwvaezjmhgfnzx
prtkqyluitsocwvaezqzhgfndx
prtkqkauibsorwvaezjmhgfndx
prtkqyluibsocwvaezfmftfndx
prtkiybuibsocwvaezjkhgfndx
prtkzyluibsocwgaezjmvgfndx
prtkqyluibsocwvaezjmhgqnxg
prtkqyluimsocwvauzjwhgfndx
prtkqyluibsacwgaezjmhgfndd
pwtkuyluibsccwvaezjmhgfndx
prtkqyluibsoawvaezjmvgfnlx
prtkqyluabsocwwaezjmhgftdx
patkqylnibsocwvaezjmhgfnox
prtkqyluibsocwlaxzkmhgfndx
pbtkqpluibsfcwvaezjmhgfndx
prtkqyluibsoywsaezjmhgxndx
prtkqyluibfocwvaezjyhgfhdx
pltbqylcibsocwvaezjmhgfndx
prtkdyluiisocwvvezjmhgfndx
prtkqkxuibsokwvaezjmhgfndx
prtkqyluibsoawvaezzmhgfndm
petkqyluibsgcwvaezjmhgfndu
prtkqyluibsoyxvaezjmlgfndx
prtkqyluibxocwvaezgmhnfndx
prtkikluibsocwvwezjmhgfndx
prbkqyluibsocwvaezjhhgfnux
prtkqylufbsxcwvaezjmhgfnfx
prtkqyluibsdcdvaezjmhgxndx
potkiyluibsocwvaezjmhkfndx
prtkqyluiosocsvhezjmhgfndx
prtkqyluibsocqbaezomhgfndx
prtihyluibsocwvaeujmhgfndx
prtuquruibsocwvaezjmhgfndx
prtkqyloibsocwvaeztmhifndx
ertuqyluibsocwvaeajmhgfndx
"""

if __name__ == '__main__':
    print(day2_1(inp))
    print(day2_2(inp))
