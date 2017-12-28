# Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a
# function answer(n, b) which returns the length of the ending cycle of the algorithm above starting with n. For instance, in the example
# above, answer(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3. If the algorithm reaches
# a constant, such as 0, then the length is 1.


def answer(n, b):
    global k
    k = len(n)
    cycle_l = []
    cycle_re = []

    while True:
        x_list = list(n)
        x = "".join(sorted(x_list, reverse=True))
        y = "".join(sorted(x_list))

        xx = convert_to_base10_int(x, b)
        yy = convert_to_base10_int(y, b)
        z_int = xx - yy
        z_str = convert_from_base10_str(z_int, b)

        print("x = {}, y = {}, xx = {}, yy = {}, z_int = {}".format(x, y, xx, yy, z_int))

        if z_str not in cycle_l:
            cycle_l.append(z_str)
            n = z_str
        else:
            if z_str in cycle_re:
                cycle_end = len(cycle_re)
                break
            cycle_l.append(z_str)
            cycle_re.append(z_str)
            n = z_str
    return cycle_end


def convert_from_base10_str(num, base):
    n_int = num
    cycle_bl = []
    cycle_bb = []
    nbi = 99
    while nbi != 0:
        cb = n_int % base
        cbi = int(cb)
        cycle_bl.append(cbi)
        nb = n_int / base
        nbi = int(nb)
        cycle_bb.append(nbi)
        n_int = nbi
    base_num = ''.join(str(b_int) for b_int in cycle_bl)[::-1]

    return base_num


def convert_to_base10_int(num_str, base):
    n_len = len(num_str)
    d_list = list(num_str)

    nbt = []
    base10 = 0

    for dig_it in d_list:
        n_len -= 1
        nb_i = int(dig_it)*(base**n_len)
        nbt.append(nb_i)

    for digi_t in nbt:
        base10 = digi_t + base10

    return base10


def base_pad(b_pad):
    b_pad = str(b_pad)
    b_len = len(b_pad)
    if b_len < k:
        badd_list = list(b_pad)
        b_add = k - b_len
        while b_add > 0:
            badd_list.insert(0, '0')
            b_add -= 1
        b_pad = "".join(badd_list)
    elif b_len > k:
        bdel_list = list(b_pad)
        del bdel_list[0]
        b_pad = "".join(bdel_list)
    else:
        pass
    return b_pad


b = 3
n = "210022"

cycle = answer(n, b)
print("Cycle Break {}".format(cycle))


#     (string) n = "1211"
#     (int) b = 10
# Output:
#     (int) 1
#
#     (string) n = "210022"
#     (int) b = 3
# Output:
#     (int) 3