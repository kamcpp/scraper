let output =
        std::process::Command::new("./scrape.sh")
            .current_dir("/src")
            .output()
            .expect("Failed to execute domain scraper script");
    let domains_output = String::from_utf8(output.stdout).unwrap();
    let mut scraped_domains = Vec::new();
    let tokens: Vec<&str> = domains_output.split(",").collect();
