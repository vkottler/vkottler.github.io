use std::path::PathBuf;
use std::str::FromStr;
use structopt::StructOpt;

#[derive(Debug)]
enum FileType {
    JSON,
    TOML,
    YAML,
    SVG,
}

impl FromStr for FileType {
    type Err = std::string::String;
    fn from_str(file_type: &str) -> Result<Self, Self::Err> {
        let mut str_type = String::from(file_type);
        str_type.make_ascii_lowercase();
        match str_type.as_str() {
            "json" => Ok(FileType::JSON),
            "svg" => Ok(FileType::SVG),
            "toml" => Ok(FileType::TOML),
            "yaml" => Ok(FileType::YAML),
            _ => Err(format!("'{}' not a valid file type", file_type)),
        }
    }
}

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

    Ok(())
}
