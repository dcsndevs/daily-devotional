$(document).ready(function() {
    // Fetch the JSON file containing the books and chapters data
    $.getJSON('/static/bible.json', function(data) {
        // Define variables to store books and chapters data
        var books = [];
        var chapters = {};

        // Iterate through each entry in the JSON data
        data.forEach(function(entry) {
            // Add book to books array
            books.push(entry.book);

            // Add chapters for each book to chapters object
            chapters[entry.book] = [];
            entry.chapters.forEach(function(chapter) {
                chapters[entry.book].push(chapter.chapter);
            });
        });

        // Populate book options
        var bookSelect = $('#book-select');
        
        books.forEach(function(book) {
            bookSelect.append($('<option>', {
                value: book,
                text: book
            }));
        });

        // Update chapter options when a book is selected
        bookSelect.change(function() {
            var selectedBook = $(this).val();
            var chapterSelect = $('#chapter-select');
            chapterSelect.empty();  // Clear existing options

            chapters[selectedBook].forEach(function(chapter) {
                chapterSelect.append($('<option>', {
                    value: chapter,
                    text: 'Chapter ' + chapter
                }));
            });
        });
    });
    // Handle form submission
    $('#bible-form').submit(function(e) {
        e.preventDefault();
        
        var selectedBook = $('#book-select').val();
        var selectedChapter = $('#chapter-select').val();
        
        //Fetch scripture content from API
        var apiUrl = 'https://bible-api.com/' + selectedBook + ':' + selectedChapter;

        $.get(apiUrl, function(data) {
            var title = data.reference;
            var verses = data.verses;
            var htmlContent = '';
            verses.forEach(function(verseData) {
                var verse = verseData.verse;
                var text = verseData.text;
                htmlContent += '<p><strong>' + verse + '.</strong> ' + text + '</p>';
            });

            // Display verses in the HTML element
            $('#scripture-title').text(title);
            $('#scripture-content').html(htmlContent);

            });

        

    });
});