from pathlib import Path
import json
def chunk_documents(docs_folder="docs"):
    all_chunks = []
    for filepath in Path(docs_folder).glob("*.text"):
        character = filepath.stem
        text = filepath.read_text(encoding="utf-8").replace('\r\n', '\n')
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        for i, para in enumerate(paragraphs):
            all_chunks.append({
                "id":f"{character}_{i:03d}",
                "character": character,
                "text": para
            })

    return all_chunks

if __name__ == "__main__":
    chunks = chunk_documents()
    for c in chunks:
        print(f"\n[{c['id']}] ({c['character']})")
        print(c['text'][:120], "...")
    print(f"\nTotal chunks: {len(chunks)}")
    with open("chunks.json", "w") as f:
        json.dump(chunks, f, indent=2)