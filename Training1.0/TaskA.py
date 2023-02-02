troom, tcond = [int(i) for i in input().split()]
regimes_dict = {'freeze': f'{min(troom, tcond)}',
                'heat': f'{max(troom, tcond)}',
                'auto': tcond,
                'fan': troom}
print(regimes_dict[input().lower()])
