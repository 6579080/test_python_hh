# def score(cf, *scores):
#     for i in scores:
#         print(cf * i)
#         # print(i)
#
# cf = 0.2
# scores = [4,5,4]
#
#
# score(cf, scores)


# for k in scores:
#     print(k * cf)

# def score(cf: float, scores: list):
#     for i in scores:
#         print(cf * i)
#         # print(i)
#
# cf = 0.2
# scores = [4,5,4]
#
#
# score(cf, scores)


# def score(cf, *scores):
#     for i in scores:
#         print(cf * i)
#         # print(i)
#
# cf = 0.2
# scores = [4,5,4]
#
#
# score(cf, *scores)


# !!!!!
# замена def score(cf, *score): на def score(cf: float, *scores: list):
def score(cf: float, *scores: list):
    for i in scores:
        print(cf * i)
        # print(i)

cf = 0.2
scores = [4,5,4]


score(cf, scores)