use std::fs::File;
use std::path::PathBuf;
use std::io::Write;
use structopt::StructOpt;

#[derive(Debug, StructOpt)]
#[structopt(
    name = "svg-gen",
    about = "An SVG (scalable vector graphic) file generator."
)]
struct Opt {
    #[structopt(parse(from_os_str), default_value = "out.svg", help = "TODO")]
    output: PathBuf,
}

fn main() -> std::io::Result<()> {
    let opt = Opt::from_args();

    println!("{:?}", opt.output.extension());

    // TODO, add svg extension if it's missing

    let mut file = File::create(opt.output)?;

    writeln!(file, "Hello, {}!", "world")?;

    file.sync_all()?;
    Ok(())
}
