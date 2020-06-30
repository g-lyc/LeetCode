// leetcode 58
// Author:lyc
package main

import (
	"fmt"
	"strings"
)

func lengthOfLastWord(s string) int {

	s = strings.Trim(s, " ")
	count := 0

	if len(s) == 0 {
		return 0
	}

	for i := len(s) - 1; i >= 0; i-- {

		if s[i] == ' ' {
			break
		}

		count += 1

	}

	return count

}

func main() {

	s := "ttt sss"
	res := lengthOfLastWord(s)
	fmt.Println(res)

}
