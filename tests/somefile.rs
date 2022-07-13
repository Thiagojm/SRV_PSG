// rustimport:pyo3

//: [dependencies]
//: ferris-says = "0.2"

use pyo3::prelude::*;
use ferris_says::say; // from the previous step
use std::io::{stdout, BufWriter};

#[pyfunction]
fn square(x: i32) -> PyResult<i32> {
    Ok(x * x)
}

#[pyfunction]
fn fib(n: usize) -> usize {
    if n <= 1 {
        return n;
    }
    fib(n-1) + fib(n-2)
}

#[pyfunction]
fn desenho() {
    let stdout = stdout();
    let message = String::from("Hello fellow Rustaceans!");
    let width = message.chars().count();

    let mut writer = BufWriter::new(stdout.lock());
    say(message.as_bytes(), width, &mut writer).unwrap();
}