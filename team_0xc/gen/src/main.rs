use serde::Serialize;
use noise::{NoiseFn, Perlin, Seedable};
use rand::random;
use std::fs::File;
use std::io::Write;

#[derive(Serialize, Debug)]
enum HeadState {
    LEFT,
    RIGHT,
    CENTER
}

#[derive(Serialize, Debug)]
enum ArmState {
    UP,
    MIDDLE,
    DOWN
}

#[derive(Serialize, Debug)]
struct Person {
    head: HeadState,
    left_arm: ArmState,
    right_arm: ArmState,
}

#[derive(Serialize, Debug)]
struct Dance {
    name: String,
    speed: u64,
    moves: Vec<Vec<Person>>
}

fn main() {
    let perlin = Perlin::new();
    perlin.set_seed(random());

    let interval: u64 = 500 as u64;
    let num_iterations = 10;
    let num_people = 3;

    let mut time: u64 = 0 as u64;
    let mut i = 0;

    let mut dance = Dance {
        name: "aaaaa".to_string(),
        speed: interval,
        moves: vec![]
    };

    while i < num_iterations {
        let x = time as f64 * 5.768472;
        let y = i as f64 * 6.7473;
        let mut j = 0;

        let mut state = vec![];

        while j < num_people {
            let z = j as f64 * 9.5737;

            let head = perlin.get([x, y, z, 2.8]);
            let l_arm = perlin.get([x, y, z, 7.9]);
            let r_arm = perlin.get([x, y, z, -3.2]);

            let head_state = if head < -0.2 {
                HeadState::LEFT
            } else if head > 0.2 {
                HeadState::RIGHT
            } else {
                HeadState::CENTER
            };

            let left_arm_state = if l_arm < -0.2 {
                ArmState::UP
            } else if head > 0.2 {
                ArmState::DOWN
            } else {
                ArmState::MIDDLE
            };

            let right_arm_state = if r_arm < -0.2 {
                ArmState::UP
            } else if head > 0.2 {
                ArmState::DOWN
            } else {
                ArmState::MIDDLE
            };

            let person = Person {
                head: head_state,
                left_arm: left_arm_state,
                right_arm: right_arm_state,
            };

            state.push(person);

            j += 1;
        }
        i += 1;
        time += interval;

        dance.moves.push(state);
    }

    let serialized = serde_json::to_string(&dance).unwrap();
    let mut file = File::create("aaaa.txt").unwrap();
    file.write_all(serialized.into_bytes().as_slice());
}
