package main

// https://leetcode.com/problems/longest-common-subsequence/
func longestCommonSubsequence(text1 string, text2 string) int {
	var subseq [1000][1000]int
	for i := 0; i < len(text1); i++ {
		for j := 0; j < len(text2); j++ {
			if text1[i] == text2[j] {
				if i == 0 || j == 0 {
					subseq[i][j] = 1
				} else {
					subseq[i][j] = subseq[i-1][j-1] + 1
				}
			} else {
				if i == 0 && j != 0 {
					subseq[i][j] = subseq[i][j-1]
				} else if i != 0 && j == 0 {
					subseq[i][j] = subseq[i-1][j]
				} else if i != 0 && j != 0 && subseq[i-1][j] >= subseq[i][j-1] {
					subseq[i][j] = subseq[i-1][j]
				} else if i != 0 && j != 0 {
					subseq[i][j] = subseq[i][j-1]
				}
			}
		}
	}
	return subseq[len(text1)-1][len(text2)-1]
}
