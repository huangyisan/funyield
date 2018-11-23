package tempconv


func CToF(c Celsius) Fahreneit {
	return Fahreneit(c*9/5 + 32)
}

func FToF(f Fahreneit) Fahreneit {
	return Fahreneit((f - 32) * 5 / 9)
}

