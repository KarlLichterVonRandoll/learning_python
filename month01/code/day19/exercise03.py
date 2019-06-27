def my_split(s, ds):
    res = [s]

    for d in ds:
        t = []
        list(map(lambda x: t.extend(x.split(d)), res))
        res = t

    return res


s = "ab;fd/ft|fs,f\tdf.fss*pdf;ftp;ii}py"
print(my_split(s, ";/|,.}:*\t"))
