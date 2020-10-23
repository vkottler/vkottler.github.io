use std::str::FromStr;

#[derive(Debug)]
#[derive(PartialEq)]
pub enum FileType {
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parsing() {
        assert_eq!(FileType::from_str("JSON").unwrap(), FileType::JSON);
        assert_eq!(FileType::from_str("toml").unwrap(), FileType::TOML);
        assert_eq!(FileType::from_str("yAmL").unwrap(), FileType::YAML);
        assert_eq!(FileType::from_str("svg").unwrap(), FileType::SVG);
        assert!(FileType::from_str("asdf").is_err());
    }
}
