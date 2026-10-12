
import csv
import logging
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_FILE = "cleaned_posts.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# EXTRACT

def extract_data(url):
    all_posts = []
    page = 1
    page_size = 20

    while True:
        response = requests.get(
            url,
            params={"_page": page, "_limit": page_size},
            timeout=30
        )

        response.raise_for_status()
        posts = response.json()

        if not posts:
            break

        all_posts.extend(posts)

        logging.info(
            "Page %s: extracted %s posts",
            page,
            len(posts)
        )

        page += 1

    return all_posts



# TRANSFORM

def transform_data(posts):
    cleaned_posts = []
    rejected_count = 0

    for post in posts:
        try:
            post_id = int(post["id"])
            user_id = int(post["userId"])
            title = post["title"].strip()
            body = post["body"].strip()

            if not title or not body:
                rejected_count += 1
                continue

            cleaned_posts.append({
                "id": post_id,
                "userId": user_id,
                "title": title,
                "body": body
            })

        except (KeyError, TypeError, ValueError, AttributeError):
            rejected_count += 1

    return cleaned_posts, rejected_count


# LOAD
def load_data(posts, output_file):
    if not posts:
        logging.warning("No records to write.")
        return

    fieldnames = ["id", "userId", "title", "body"]

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts)

    logging.info("Wrote %s records to %s", len(posts), output_file)


# ORCHESTRATE
def main():
    logging.info("ETL pipeline started")

    try:
        posts = extract_data(API_URL)
        cleaned_posts, rejected_count = transform_data(posts)
        logging.info("Records extracted: %s", len(posts))
        logging.info("Records accepted: %s", len(cleaned_posts))
        logging.info("Records rejected: %s", rejected_count)

        load_data(cleaned_posts, "cleaned_posts.csv")

        logging.info("Pipeline completed successfully")

    except (requests.RequestException, ValueError, OSError):
        logging.exception("ETL pipeline failed")
        print("ETL failed. Review the error message.")


if __name__ == "__main__":
    main()
