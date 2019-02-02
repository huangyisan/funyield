package tempconv

import "fmt"

type Celsius float64
type Fahreneit float64

const (
	AbsoluteZeroC Celsius = -273.15
	FreesingC Celsius = 0
	boilingC Celsius = 100
)

func (c Celsius) String() string {
	return fmt.Sprintf("%g°C", c)
}

func (f Fahreneit) String() string {
	return fmt.Sprintf("%g°F", f)
}

