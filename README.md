# A Talking Clock created by Alice V., Amber L., Brandi H., Jingxuan Y., and Wenjun M.

## Project Description
This is a multilingual talking clock developed for a combined assignment in the Programming and Introduction to Voice Technology courses in the first term of the MSc Voice Technology program at Rijksuniversiteit Groningen - Campus Fryslân. The clock speaks the time aloud in 6 languages: Dutch, American English, Italian, Mandarin Chinese, German, and Latin. The German and Latin voices are synthesized voices, and the remaining voices are spoken by native speakers. Each language is spoken in its own respective linguistic rules for telling time. 

## Installation Requirements
Installation of `Python 3.6` is minimally required, however, installation of `Python 3.11` is recommended. Python can be downloaded from the following link: https://www.python.org/downloads/

A stable internet connection is required to run the program, as the program uses an API call to display weather information.

## Installation Instructions
1. Click on the green `Code` button at the top of the repository, then click `Download ZIP`.
2. Extract the ZIP to the location where you want to install it on your computer.
3. Open the terminal/command prompt and navigate to the file path of the extracted ZIP.
4. Run `pip install -r requirements.txt` to install the dependencies required.

## How to Run the Program
While in the same directory as the extracted ZIP, run `python main.py` in the terminal. This will open the GUI for the talking clock program.

The clock displays the following information: current weather conditions, current time, and current date. The background color of the application is a constantly changing gradient on a 12 hour cycle. It changes with each minute.

To speak the current time, press the button at the bottom of the screen which corresponds to the desired language.

At the top of the clock there is a toggle for dark mode. Dark mode is not available while using the `Display Random Time` button, as the purpose of the `Display Random Time` button is to demonstrate the background gradient. Additionally, random times cannot be spoken, as they only affect the GUI (there is no value stored). To return the clock to its original state, press the `Display Current Time` button. 

## Supported Languages
- Dutch
- English
- Italian
- Mandarin Chinese
- German
- Latin

## Linguistic Rules for Telling Time

### Dutch
The Dutch linguistic system for telling time anchors itself on certain points in time: the hour and the 15 minute increments (:15, :30, :45). 

In Dutch, whole hours are quite similar to English; however, instead of using the word 'o'clock', "uur" is used which means 'hour'. The use of 'half past' is a bit different compared to English. The use of "half" is actually followed by the next hour. For example, half past 1 in Dutch is "half 2". 'A quarter to' and 'a quarter past' are used the same compared to English. A quarter past 1, is "kwart over 1" and a quarter to is "kwart voor". 

Minutes before a round hour are used in this way: 60 is subtracted by the minutes of the current time. "Het is 8 voor 9", would be translated in English to: 'It is 8 to 9' (It is 8:52). This can also be used after a whole hour. "Het is 5 over 3" would be 'It is 5 past 3' in English. 

For half hours, this system is also used, but then "half" is added (remember when using "half", the next hour is used). For example, 3:40 in Dutch would be read as: "Het is 10 over half 4". The literal translation in English would be: 'It is 10 past half past 3' (It is 3:40). The same logic is used before a half hour. For example, 1:25 in Dutch would be read as: "Het is 5 voor half 2". The literal translation in English would be: 'It is 5 to half past 1' (It is 1:25). 

Generally, from minute 10 of an hour until minute 20 of an hour and minute 40 until minute 50, a rounding system is used. If it is 3:13, it would be rounded to 3:15 and 3:12 would be rounded to 3:10. There are no strict requirements for rounding time in this way, but this is the most widely accepted methodology.

### American English
Speaking time in American English, at its base level, is very simple and straightforward. If it is the top of the hour, one would say: "It is (hour) o'clock a.m./p.m. For example, at 5:00 p.m., the time would be read as "It is 5 o'clock p.m. When minutes are involved, the time is read as: "It is (hour) (minute) a.m./p.m. For example, 5:21 p.m. would be read as: "It is five twenty-one p.m." The only thing to note when reading minutes is that minutes 01-09 are read as "oh (minute)". For example, 5:06 p.m. would be read as "It is five oh six p.m."

There are some short form ways of telling time in American English, such as 12:00 a.m. being "midnight" and 12:00 p.m. being "noon". Additionally, Americans often use terms such as "half past", which indicates 30 minutes over the current hour. For example, 5:30 p.m. could be read as: "half past five". Similarly, Americans often use "quarter till" as a way to indicate 15 minutes until the next hour. For example, 6:45 p.m. could be read as "quarter till 7". However, the Multilingual Talking Clock application does not support these short form ways of telling time.

### Italian
The Italian language has a linguistic time system similar to English, usually telling first the hour and then the minutes, and having expressions to indicate the half and the quarters of the hours. The former is expressed through the word “mezzo” or “mezza”, depending on the variety, while the latter is translated to “un quarto”. Hours are usually indicated using simple numbers, except for 01:00 a.m./p.m., for which the standard form of the cardinal number "uno" is not used, but the female form “una”. Additionally, the Multilingual Talking Clock does not use the number to indicate 12:00 a.m./p.m., but the more spread expressions “mezzogiorno” (midday) and “mezzanotte” (midnight).

The 12-hour format is commonly used in Italy, but in formal contexts and some regional varieties, the 24-hour format is preferred. Even when using the 12-hour format, in Italian, it is not common to refer to the time using expressions equivalent to a.m. and p.m., hence the Multilingual Talking Clock does not include these references.

Instead of using all the numbers to indicate the exact minute, the Multilingual Talking Clock opts for a simplified approach to telling time in Italian by only indicating it every five minutes. Hence, the clock will not tell the exact minutes, but the closest multiple of five. For example, if the time is 4:08 p.m. it will say "quattro e dieci" (lit. en. "ten past four"). These choices reflect the most common way of telling time in Italian, despite using numbers being perfectly acceptable in the aforementioned cases. It is worth noting that these expressions are not pan-Italian, but rather based on the Tuscan variant of Italian.

### Mandarin Chinese
The logic of telling time in Chinese usually describes the current time by hour and minute. In Chinese, the following information is usually included: The hour is usually expressed in a 12-hour format, such as “shang wu 9 dian” (9:00 am) or "xia wu 3 dian” (3:00 pm). Minutes are usually expressed in Arabic numerals, followed by “fen”(minute), e.g. "9 dian 15 fen” (9:15) or "3 dian 45 fen” (3:45). When it’s on the hour, “zheng” (o’clock) will be added after the hour, e.g. “9 dian zheng” (9:00 o’clock). 

Additionally, the phrase "xian zai shi" (the current time is) is used to introduce a description of the time. To distinguish AM or PM, “shang wu” (AM) and “xia wu” (PM) are used at the beginning of the time description.

### Latin and German
The authors of the Multilingual Talking Clock program do not speak German or Latin. Therefore, the linguistic systems listed below pertain specifically to how the time is spoken within the program and should not necessarily be referenced as legitimate rules for speaking the time in the respective languages.

The Multilingual Talking Clock speaks time in German in the following format: "It is" + hour + "hour and" + minutes + "minutes". It translates directly in German to "Es ist" + hour + "Uhr" + minutes + "minuten.

For Latin, the translation is slightly more complex as the syntactic structure of the Latin sentence is reversed. The resulting sentence will be "Hora est" + hour (expressed using cardinal numbers) + "et" + minutes (expressed using cardinal numbers) + "minuta". The literal translation would be: "The hour is ___ and ___ minutes".

## GDPR Compliance
The recordings for American English, Dutch, Italian and Mandarin Chinese have been done complying to the General Data Protection Regulation. The five participants have signed an informed consent form that is stored in the folder "GDPR_informed_consent", together with the empty template. All the recordings used have been pseudonimysed to guarantee the highest degree of privacy possible.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

