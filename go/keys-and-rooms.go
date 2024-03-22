package main

// https://leetcode.com/problems/keys-and-rooms/
func canVisitAllRooms(rooms [][]int) bool {
	if rooms == nil {
		return false
	}
	if len(rooms) == 1 {
		return true
	}

	var keyChain []int
	keyChain = append(keyChain, 0)
	var keySet = map[int]bool{0: true}

	for len(keyChain) > 0 {
		if len(keySet) == len(rooms) {
			return true
		}
		key := keyChain[0]
		for _, newKey := range rooms[key] {
			if !keySet[newKey] {
				keyChain = append(keyChain, newKey)
				keySet[newKey] = true
			}
		}
		keyChain = keyChain[1:]
	}
	return false
}
