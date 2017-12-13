import unittest


'''
시험 문제 2) 장식자 구현하기

- 다수의 인자를 받아, 2개의 인자로 변환하여 함수를 호출토록 구현
- 첫번째 인자 : 홀수의 합
- 두번째 인자 : 짝수의 합

모든 테스트가 통과하면, 다음과 같이 출력됩니다.


쉘> python final_2.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
'''


def divider(fn):
    def wrap(*args):
        odd = sum(i for i in args if i%2!=0)
        even = sum(i for i in args if i%2==0)
        return fn(odd, even)
    return wrap


########################################
#
# 아래는 수정하지마세요.
#
########################################

@divider
def mysum(x, y):
    return x + y


@divider
def mymultiply(x, y):
    return x * y


@divider
def mypow(x, y):
    return x ** y


class TestFinalExam(unittest.TestCase):
    def k__test_mysum(self):
        self.assertEqual(mysum(1, 2), 3)
        self.assertEqual(mysum(1, 2, 3), 6)
        self.assertEqual(mysum(1, 2, 3, 4), 10)
        self.assertEqual(mysum(1, 2, 3, 4, 5), 15)
        self.assertEqual(mysum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 55)
        self.assertEqual(mysum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1001), 1156)

    def test_mymultiply(self):
        # self.assertEqual(mymultiply(1, 2), 2)             #     1 * 2
        # self.assertEqual(mymultiply(1, 2, 3), 8)          # (1+3) * 2
        # self.assertEqual(mymultiply(1, 2, 3, 4), 24)      # (1+3) * (2+4)
        # self.assertEqual(mymultiply(1, 2, 3, 4, 5), 54)   # (1+3+5) * (2+4)
        # self.assertEqual(mymultiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 750)
        self.assertEqual(mymultiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1001), 133380)

        # (1 + 3 + 5 + 7 + 8 + 9) * (2 + 4 + 6 + 8 + 10 + 100 + 1001)

    def test_mypow(self):
        # self.assertEqual(mypow(1, 2), 1)                 #       1 ** 2
        # self.assertEqual(mypow(1, 2, 3), 16)             #   (1+3) ** 2
        # self.assertEqual(mypow(1, 2, 3, 4), 4096)        #   (1+3) ** (2+4)
        # self.assertEqual(mypow(1, 2, 3, 4, 5), 531441)   # (1+3+5) ** (2+4)
        # self.assertEqual(mypow(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 867361737988403547205962240695953369140625)
        pass


if __name__ == '__main__':
    unittest.main()

