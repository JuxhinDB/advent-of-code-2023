use anyhow::Result;
use std::{collections::BTreeMap, env::args, fs::read_to_string};

type Source = u32;
type Destination = u32;
type Length = u32;
type Map<'a> = (&'a str, BTreeMap<Source, (Destination, Length)>);

fn main() -> Result<()> {
    let file_path = args()
        .nth(1)
        .ok_or(anyhow::anyhow!("missing file path argument"))?;

    let content = read_to_string(file_path)?;
    let lines = content.lines().collect::<Vec<&str>>();

    // Parse the seeds and group into pairwise
    let seeds = lines[0]
        .split(' ')
        .skip(1)
        .collect::<Vec<&str>>()
        .as_slice()
        .chunks(2)
        .map(|chunk| {
            (
                chunk[0].parse::<u32>().unwrap(),
                chunk[1].parse::<u32>().unwrap(),
            )
        })
        .collect::<Vec<(u32, u32)>>();

    let mut map_alamac: Vec<Map> = vec![
        ("seed-to-soil", BTreeMap::new()),
        ("soil-to-fertilizer", BTreeMap::new()),
        ("fertilizer-to-water", BTreeMap::new()),
        ("water-to-light", BTreeMap::new()),
        ("light-to-temperature", BTreeMap::new()),
        ("temperature-to-humidity", BTreeMap::new()),
        ("humidity-to-location", BTreeMap::new()),
    ];

    let mut cur_map_str: Option<&str> = None;
    for line in lines.iter().skip(1) {
        let mut record = line.split(' ');

        if line.contains("map") {
            cur_map_str = Some(
                record
                    .nth(0)
                    .ok_or(anyhow::anyhow!("map record malformed"))?,
            );
            continue;
        }

        if let Ok(mapping) = record
            .into_iter()
            .map(|v| v.parse::<u32>().map_err(|e| anyhow::anyhow!(e)))
            .collect::<Result<Vec<u32>>>()
        {
            let (dst, src, len) = (mapping[0], mapping[1], mapping[2]);
            for (key, map) in map_alamac.iter_mut() {
                if key == &cur_map_str.unwrap() {
                    map.insert(src, (dst, len));
                }
            }
        }
    }

    let mut min_loc = u32::MAX;

    seeds.into_iter().for_each(|seed| {
        println!("testing range {}..{}", seed.0, seed.0 + seed.1);
        for seed in seed.0..=(seed.0 + seed.1) {
            let location = map_alamac.iter().fold(seed, |mut lookup, (_, map)| {
                for (src, (dst, len)) in map.into_iter() {
                    if (src..&(src + len)).contains(&&lookup) {
                        lookup = dst + (lookup - src);
                    }
                }

                lookup
            });

            if location <= min_loc {
                min_loc = location;
            }
        }
    });

    println!("The minimum location is {min_loc}");

    Ok(())
}
