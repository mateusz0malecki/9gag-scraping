from .infinite_scroll_scraping import get_scrolled_page_content
from models.tag import Tag
from models.meme import Meme


def get_9gag_memes_info(db):
    bs = get_scrolled_page_content('https://9gag.com/')
    meme_lists = bs.find_all('div', class_='list-stream')

    memes_to_db = []

    for meme_list in meme_lists:
        memes = meme_list.find_all('article')

        for meme in memes:
            title = meme.find('h1').get_text() if meme.find('h1') else None

            if meme.find('picture'):
                link = meme.find('picture').find('source')['srcset']
            elif meme.find('video'):
                link = meme.find('video').find('source')['src']
            else:
                link = None

            meme_tags = []
            tags_list = meme.find('div', class_='post-tag listview')
            if tags_list:
                tags = tags_list.find_all('a')
                for tag in tags:
                    meme_tags.append(tag.get_text())

            if link:
                tags_db_objects = []
                for tag in meme_tags:
                    tag_object = Tag.get_tag_by_name(db, tag)
                    if not tag_object:
                        tag_object = Tag(tag_name=tag)
                        db.add(tag_object)
                        db.commit()
                    tags_db_objects.append(tag_object)

                meme_to_db = Meme(
                    title=title,
                    link=link,
                    tags=tags_db_objects
                )
                memes_to_db.append(meme_to_db)

    db.add_all(memes_to_db)
    db.commit()
