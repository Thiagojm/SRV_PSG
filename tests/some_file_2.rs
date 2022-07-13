// rustimport:pyo3

use pyo3::prelude::*;


#[pyfunction]
fn strin_to_int(x: &str, y: i32) -> (i32, &str, i32) {
    if x.parse::<i32>().is_ok() {
        let first_el = x.parse::<i32>().unwrap();
        let second_el = "Ok";
        let third_el = y;
        println!("Piruko");
        return (first_el, second_el, third_el);
    } else {
        let first_el = 0;
        let second_el = "Error";
        let third_el = y;
        return (first_el, second_el, third_el);
    }
}

