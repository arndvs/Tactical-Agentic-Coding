import { $ } from "bun";
import { readFileSync } from "fs";

async function main() {
    try {
        const promptContent = readFileSync("programmable/prompt.md", "utf-8");

        const output = await $`claude -p ${promptContent}`.text();

        console.log(output);
    } catch (error) {
        console.error(`Error executing command: ${error}`);
        process.exit(1);
    }
}

if (import.meta.main) {
    main();
}