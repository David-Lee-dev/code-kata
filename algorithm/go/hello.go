package main

import "fmt"

type person struct {
	name     string
	age      int
	favorite []string
}

func main() {
	fav := []string{"buritto"}
	jh := person{name: "jordan", age: 20, favorite: fav}

	fmt.Println(jh)
}
