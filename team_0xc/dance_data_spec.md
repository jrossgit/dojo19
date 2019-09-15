# Dance data specification

For the purposes of this project a dance is considered a line of people
a head and two arms, each person in capable of moving their head left and
right and their arms up an down.

## Person object
A person object is as such

```json
{
  "head": "CENTER" // One of LEFT, RIGHT, CENTER,
  "left_arm": "UP" // One of UP, MIDDLE_UP, MIDDLE, MIDDLE_DOWN, DOWN
  "right_arm": "DOWN" // Same as above
}
```

## Person list
A person list is as such:

```json
[{`Person object`}, {`Person object`}, ...]
```

## Dance object
Each dance shall be stored in one JSON file
```json
{
  "name": "a name",
  "speed": "1000", // Number of ms between states
  "moves": [
    // Person list
    // Person list
    // Person list
  ]
}
```