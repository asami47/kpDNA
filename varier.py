def mix_dna_samples(sample1, sample2, percentage1, percentage2):
    if len(sample1) != len(sample2):
        raise ValueError("Both samples must have the same number of values.")
    if percentage1 + percentage2 != 100:
        raise ValueError("The sum of percentages must be 100.")

    p1 = percentage1 / 100.0
    p2 = percentage2 / 100.0


    mixed_sample = [p1 * s1 + p2 * s2 for s1, s2 in zip(sample1, sample2)]
    return mixed_sample

sample1 = [0.0975192835, 0.0819759221, -0.040777059899999996, -0.0200902404, -0.0367183316, 0.0011231836, 0.0034904220999999996, -0.0035838815000000003, -0.031865943, -0.0172542245, -0.0017640006, 0.0015342849999999998, -0.0027793995, -0.0045964081, 0.0034223879999999997, 0.004776615, -0.0027164951, 0.0014077371, 0.0008206161, -0.007078702099999999, -0.0008107473999999998, -0.0026306454999999998, -0.0012030291, -0.0014719110000000002, 0.0016016465999999997
]

sample2 = [0.10142091049999999, 0.08079480630000001, -0.019818449699999994, -0.005271601200000001, -0.029137844800000003, 0.0035756108, 0.0031210162999999996, -0.0017649645000000001, -0.024653178999999997, -0.014789903499999998, -0.0021300218000000004, -0.0009499049999999999, -0.0007525285000000001, -0.009300904300000001, 0.009367664000000001, 0.008206755000000001, -0.0044836453, 0.0022020713000000004, 0.0030735282999999995, -0.0052997363, -0.0034549121999999993, 0.00010695349999999984, -0.0011274473, 0.0008198969999999999, 0.31196489980000003
]

mixed_sample = mix_dna_samples(sample1, sample2, 50, 50)
print(mixed_sample)