use std::collections::HashMap;

#[derive(Debug)]
struct Primitive {
    name: String,
    attributes: HashMap<String, String>,
}

impl Primitive {
    pub fn serialize() -> String {
        String::from("")
    }
}

#[derive(Debug)]
pub struct Document {
    version: String,
    xmlns: String,
    height: u32,
    width: u32,
    origin: (u32, u32),
    children: Vec<Primitive>,
}

impl Document {
    pub fn new() -> Self {
        Default::default()
    }

    pub fn set_viewbox(&mut self, height: u32, width: u32, origin: (u32, u32)) {
        self.height = height;
        self.width = width;
        self.origin = origin;
    }

    pub fn serialize(&self) -> String {
        let result = format!("<svg version=\"{}\" xmlns=\"{}\" />", self.version, self.xmlns);
        String::from(result)
    }
}

impl Default for Document {
    fn default() -> Self {
        Self {
            version: String::from("1.0"),
            xmlns: String::from("http://www.w3.org/2000/svg"),
            height: 512,
            width: 512,
            origin: (0, 0),
            children: Vec::new(),
        }
    }
}
