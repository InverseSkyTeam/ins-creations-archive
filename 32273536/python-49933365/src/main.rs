use std::io::stdin;
use std::io::stdout;
use std::io::Write;

peg::parser!(
    grammar number_parser() for str {
        rule number() -> u32
            = n:$(['0'..='9']+) {? n.parse().or(Err("Invalid Integer."))}
        rule whitespace() = quiet!{[' ' | '\n' | '\t']+}
        pub rule arithmetic() -> u32 = precedence!{
            x:(@) whitespace()? "+" whitespace()? y:@ { x + y }
            x:(@) whitespace()? "-" whitespace()? y:@ { x - y }
            --
            x:(@) whitespace()? "*" whitespace()? y:@ { x * y }
            x:(@) whitespace()? "/" whitespace()? y:@ { x / y }
            --
            x:@ whitespace()? "^" whitespace()? y:(@) { x.pow(y) }
            --
            whitespace()? n:number() whitespace()? { n }
            whitespace()? "(" whitespace()? e:arithmetic() whitespace()? ")" whitespace()? { e }
        }
        pub rule list() -> Vec<u32>
            = "[" l:(number() ** ",") "]" { l }
    }
);

fn main() {
    let mut string_buf = String::new();
    loop {
        let _ = stdout().write("Expr>>>".as_bytes()).unwrap();
        stdout().flush().unwrap();
        stdin()
            .read_line(&mut string_buf)
            .expect("Unable to readline.");
        if string_buf.trim_end() == "exit" {
            break;
        }
        let result = number_parser::arithmetic(string_buf.trim_end()).expect("Invalid Expression.");
        println!("<<<Result: {}", result);
    }
}
