package main

import (
	"fmt"
	"reflect"
)

func main() {
	var a, b float32 = 4, 3
	var s float32
	s = a / b
	fmt.Println(s)

	if (1==1) && true && true {
		if true{
			println("相等, 相等")
		}
		println("相等")
	} else{
		println("不相等")
	}

	var c uint = 60
	var d uint = 13
	var e uint = 0

	e = c & d
	println(e)

	e = 1 << 2
	println(e)

	e = 4
	ptr := &e
	println(e, "     ", ptr)

    f := reflect.TypeOf(e)
    println(f.Name())
	v2 := "test"
    println(reflect.TypeOf(v2))

	var g int
	switch e {
	case 20: println("no"); g = 111
	case 4: println("yes"); g = 222
		println(g)
	}

	var h interface{}
	switch h.(type){
	case nil:
		println("类型正确")
	}
	sum := 0
	for i := 0; i <= 10; i++{
		sum += i
	}
	println(sum)

	for {
		sum ++
		if sum > 1000{
			println("循环退出, sum:   ", sum)
			break
		}
	}

	strings := []string{"google", "songxiyang"}
	for i, s := range strings {
		println(i, s)
	}

	i := "qweqweqwe"
	println(i)

	numbers := [6]int {1,2,3,4}
	for i, x := range numbers{
		println(i, x)
	}

	aa, bb := 1, 3
	ret1, ret2 := aaa(aa, bb)
	println("是", ret1, ret2)
	println("aa, bb", aa, bb)

	cc := &aa
	dd := *cc
	println(*cc, "      ", dd)

	const ee int = 6
	var ff int = 7
	cc = &ff
	dd = *cc
	println(*cc, "      ", dd, ee)

	println(max(aaa(3, 2)))

	var balance123 = [...] int{1: 1.0,5: 2.0}
	for i, v :=range balance123{
		balance123[i] = v + 100
		println(i, balance123[i])
	}


}
func max(num1 int, num2 int) int {
	/* 声明局部变量 */
	var result int

	if (num1 > num2) {
		result = num1
	} else {
		result = num2
	}
	return result
}

func aaa(m, n int) (int, int) {
	ret := max(m, n)
	m, n = n, m
	println("****", m, n)
	println(ret)
	//println(balance)
	println("c")
	return ret, ret
}
