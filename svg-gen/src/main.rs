use std::path::PathBuf;
use structopt::StructOpt;

mod file_type;
use file_type::FileType;

mod svg;
use svg::Document;

#[derive(Debug, StructOpt)]
#[structopt(
    name = "svg-gen",
    about = "An SVG (scalable vector graphic) file generator."
)]
struct Opt {
    #[structopt(short, parse(from_os_str), help = "Path to the input manifest.")]
    input: PathBuf,

    #[structopt(long, help = "Input manifest type.")]
    input_type: Option<FileType>,

    #[structopt(long, default_value = "svg", help = "Output artifact type.")]
    output_type: FileType,

    #[structopt(
        short,
        parse(from_os_str),
        default_value = "out.svg",
        help = "Path to the output artifact."
    )]
    output: PathBuf,

    #[structopt(parse(from_os_str), help = "Additional include paths.")]
    include_paths: Vec<PathBuf>,
}

fn main() -> std::io::Result<()> {
    let opt = Opt::from_args();

    println!("{:?}", opt);

    let mut doc = Document::new();
    println!("{:?}", doc);

    doc.set_viewbox(0, 0, (0, 0));

    println!("{}", doc.serialize());

    Ok(())
}
