-- Keep a log of any SQL queries you execute as you solve the mystery.
theft took place on July 28, 2024 and that it took place on Humphrey Street.
.schema
CREATE TABLE crime_scene_reports (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    street TEXT,
    description TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE interviews (
    id INTEGER,
    name TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    transcript TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE atm_transactions (
    id INTEGER,
    account_number INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    atm_location TEXT,
    transaction_type TEXT,
    amount INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE bank_accounts (
    account_number INTEGER,
    person_id INTEGER,
    creation_year INTEGER,
    FOREIGN KEY(person_id) REFERENCES people(id)
);
CREATE TABLE airports (
    id INTEGER,
    abbreviation TEXT,
    full_name TEXT,
    city TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE flights (
    id INTEGER,
    origin_airport_id INTEGER,
    destination_airport_id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
    FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
);
CREATE TABLE passengers (
    flight_id INTEGER,
    passport_number INTEGER,
    seat TEXT,
    FOREIGN KEY(flight_id) REFERENCES flights(id)
);
CREATE TABLE phone_calls (
    id INTEGER,
    caller TEXT,
    receiver TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    duration INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE people (
    id INTEGER,
    name TEXT,
    phone_number TEXT,
    passport_number INTEGER,
    license_plate TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE bakery_security_logs (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    activity TEXT,
    license_plate TEXT,
    PRIMARY KEY(id)
);

select * from crime_scene_reports where street='Humphrey Street';
id=295
Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

select * from bakery_security_logs where day='28';
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 219 | 2024 | 7     | 28  | 8    | 2      | entrance | 1M92998       |
| 220 | 2024 | 7     | 28  | 8    | 2      | entrance | N507616       |
| 221 | 2024 | 7     | 28  | 8    | 2      | exit     | 1M92998       |
| 222 | 2024 | 7     | 28  | 8    | 2      | exit     | N507616       |
| 223 | 2024 | 7     | 28  | 8    | 7      | entrance | 7Z8B130       |
| 224 | 2024 | 7     | 28  | 8    | 7      | exit     | 7Z8B130       |
| 225 | 2024 | 7     | 28  | 8    | 13     | entrance | 47MEFVA       |
| 226 | 2024 | 7     | 28  | 8    | 13     | exit     | 47MEFVA       |
| 227 | 2024 | 7     | 28  | 8    | 15     | entrance | D965M59       |
| 228 | 2024 | 7     | 28  | 8    | 15     | entrance | HW0488P       |
| 229 | 2024 | 7     | 28  | 8    | 15     | exit     | D965M59       |
| 230 | 2024 | 7     | 28  | 8    | 15     | exit     | HW0488P       |
| 231 | 2024 | 7     | 28  | 8    | 18     | entrance | L93JTIZ       |
| 232 | 2024 | 7     | 28  | 8    | 23     | entrance | 94KL13X       |
| 233 | 2024 | 7     | 28  | 8    | 25     | entrance | L68E5I0       |
| 234 | 2024 | 7     | 28  | 8    | 25     | entrance | HOD8639       |
| 235 | 2024 | 7     | 28  | 8    | 25     | exit     | HOD8639       |
| 236 | 2024 | 7     | 28  | 8    | 34     | exit     | L68E5I0       |
| 237 | 2024 | 7     | 28  | 8    | 34     | entrance | 1106N58       |
| 238 | 2024 | 7     | 28  | 8    | 34     | entrance | W2CT78U       |
| 239 | 2024 | 7     | 28  | 8    | 34     | exit     | W2CT78U       |
| 240 | 2024 | 7     | 28  | 8    | 36     | entrance | 322W7JE       |
| 241 | 2024 | 7     | 28  | 8    | 38     | entrance | 3933NUH       |
| 242 | 2024 | 7     | 28  | 8    | 38     | exit     | 3933NUH       |
| 243 | 2024 | 7     | 28  | 8    | 42     | entrance | 0NTHK55       |
| 244 | 2024 | 7     | 28  | 8    | 44     | entrance | 1FBL6TH       |
| 245 | 2024 | 7     | 28  | 8    | 44     | exit     | 1FBL6TH       |
| 246 | 2024 | 7     | 28  | 8    | 49     | entrance | P14PE2Q       |
| 247 | 2024 | 7     | 28  | 8    | 49     | exit     | P14PE2Q       |
| 248 | 2024 | 7     | 28  | 8    | 50     | entrance | 4V16VO0       |
| 249 | 2024 | 7     | 28  | 8    | 50     | exit     | 4V16VO0       |
| 250 | 2024 | 7     | 28  | 8    | 57     | entrance | 8LLB02B       |
| 251 | 2024 | 7     | 28  | 8    | 57     | exit     | 8LLB02B       |
| 252 | 2024 | 7     | 28  | 8    | 59     | entrance | O784M2U       |
| 253 | 2024 | 7     | 28  | 8    | 59     | exit     | O784M2U       |
| 254 | 2024 | 7     | 28  | 9    | 14     | entrance | 4328GD8       |
| 255 | 2024 | 7     | 28  | 9    | 15     | entrance | 5P2BI95       |
| 256 | 2024 | 7     | 28  | 9    | 20     | entrance | 6P58WS2       |
| 257 | 2024 | 7     | 28  | 9    | 28     | entrance | G412CB7       |
| 258 | 2024 | 7     | 28  | 10   | 8      | entrance | R3G7486       |
| 259 | 2024 | 7     | 28  | 10   | 14     | entrance | 13FNH73       |
| 260 | 2024 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 262 | 2024 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2024 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2024 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       |
| 269 | 2024 | 7     | 28  | 10   | 42     | entrance | NRYN856       |
| 270 | 2024 | 7     | 28  | 10   | 44     | entrance | WD5M8I6       |
| 271 | 2024 | 7     | 28  | 10   | 55     | entrance | V47T75I       |
| 272 | 2024 | 7     | 28  | 11   | 6      | entrance | 4963D92       |
| 273 | 2024 | 7     | 28  | 11   | 13     | entrance | C194752       |
| 274 | 2024 | 7     | 28  | 11   | 52     | entrance | 94MV71O       |
| 275 | 2024 | 7     | 28  | 12   | 20     | entrance | FLFN3W0       |
| 276 | 2024 | 7     | 28  | 12   | 49     | entrance | 207W38T       |
| 277 | 2024 | 7     | 28  | 13   | 8      | entrance | RS7I6A0       |
| 278 | 2024 | 7     | 28  | 13   | 30     | entrance | 4468KVT       |
| 279 | 2024 | 7     | 28  | 13   | 42     | entrance | NAW9653       |
| 280 | 2024 | 7     | 28  | 14   | 18     | exit     | NAW9653       |
| 281 | 2024 | 7     | 28  | 15   | 6      | exit     | RS7I6A0       |
| 282 | 2024 | 7     | 28  | 15   | 16     | exit     | 94MV71O       |
| 283 | 2024 | 7     | 28  | 16   | 6      | exit     | WD5M8I6       |
| 284 | 2024 | 7     | 28  | 16   | 38     | exit     | 4468KVT       |
| 285 | 2024 | 7     | 28  | 16   | 42     | exit     | 207W38T       |
| 286 | 2024 | 7     | 28  | 16   | 47     | exit     | C194752       |
| 287 | 2024 | 7     | 28  | 17   | 11     | exit     | NRYN856       |
| 288 | 2024 | 7     | 28  | 17   | 15     | exit     | 13FNH73       |
| 289 | 2024 | 7     | 28  | 17   | 16     | exit     | V47T75I       |
| 290 | 2024 | 7     | 28  | 17   | 18     | exit     | R3G7486       |
| 291 | 2024 | 7     | 28  | 17   | 36     | exit     | FLFN3W0       |
| 292 | 2024 | 7     | 28  | 17   | 47     | exit     | 4963D92       |
+-----+------+-------+-----+------+--------+----------+---------------+
select * from interviews where month=7;
| 161 | Ruth        | 2024 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 162 | Eugene      | 2024 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 163 | Raymond     | 2024 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

Theif exit narrows down to:
| 260 | 2024 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 262 | 2024 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2024 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2024 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       |

select * from atm_transactions where day=28 and atm_location='Humphrey Lane' and transaction_type='withdraw';
+-----+----------------+------+-------+-----+---------------+------------------+--------+
| id  | account_number | year | month | day | atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+---------------+------------------+--------+
| 245 | 90209473       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 45     |
| 247 | 41935128       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 15     |
| 255 | 66344537       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 55     |
| 258 | 92647903       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 5      |
| 262 | 40665580       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 35     |
| 265 | 96336648       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 20     |
| 273 | 69638157       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 20     |
| 276 | 13156006       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 15     |
| 277 | 89843009       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 40     |
| 280 | 92647903       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 40     |
| 281 | 57022441       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 55     |
| 290 | 79165736       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 5      |
| 291 | 76849114       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 10     |
| 300 | 66344537       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 60     |
| 302 | 50380485       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 100    |
| 309 | 46222318       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 60     |
| 310 | 58673910       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 10     |
| 312 | 93903397       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 35     |
| 315 | 79127781       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 65     |
| 316 | 95773068       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 45     |
| 322 | 26797365       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 35     |
| 329 | 34939061       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 100    |
| 333 | 65190958       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 50     |
| 334 | 99031604       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 20     |
| 337 | 58552019       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 30     |
| 342 | 55322348       | 2024 | 7     | 28  | Humphrey Lane | withdraw         | 5      |
+-----+----------------+------+-------+-----+---------------+------------------+--------+

select * from people where id in (select person_id from bank_accounts where account_number in (select account_number from atm_transactions where day=28 and atm_location='Humphrey Lane' and transaction_type='withdraw'));
+--------+-----------+----------------+-----------------+---------------+
|   id   |   name    |  phone_number  | passport_number | license_plate |
+--------+-----------+----------------+-----------------+---------------+
| 229572 | Ernest    | (789) 555-8833 | 6216255522      | C3S4W87       |
| 274388 | Laura     | (067) 555-4133 | 1801324150      | 4406M71       |
| 274893 | Christina | (547) 555-8781 | 4322787338      | 79X5400       |
| 293753 | Ryan      | (901) 555-8732 | NULL            | 0WZS77X       |
| 336397 | Joan      | (711) 555-3007 | NULL            | L476K20       |
| 341739 | Rebecca   | (891) 555-5672 | 6264773605      | NULL          |
| 484375 | Anna      | (704) 555-2131 | NULL            | NULL          |
| 506435 | Zachary   | (839) 555-1757 | NULL            | 5810O6V       |
| 539960 | Theresa   | (190) 555-4928 | 1833124350      | 668A8SL       |
| 567218 | Jack      | (996) 555-8899 | 9029462229      | 52R0Y8U       |
| 572028 | Paul      | (357) 555-0246 | 9143726159      | R64E41W       |
| 630782 | Alexis    | (814) 555-5180 | 5310124622      | X4G3938       |
| 632023 | Amanda    | (821) 555-5262 | 1618186613      | RS7I6A0       |
| 637069 | Michelle  | (738) 555-2050 | 4590049635      | 52E25A9       |
| 652412 | Denise    | (994) 555-3373 | 4001449165      | NRYN856       |
| 704850 | Rachel    | (006) 555-0505 | NULL            | 7Z8B130       |
| 713341 | Donna     | NULL           | NULL            | 8LLB02B       |
| 757606 | Douglas   | (491) 555-2505 | 3231999695      | 1FW4EUJ       |
| 769190 | Charles   | (427) 555-0556 | 3915621712      | R12SA4D       |
| 779942 | Harold    | (669) 555-6918 | NULL            | DVS39US       |
| 837455 | Andrew    | (579) 555-5030 | NULL            | W2CT78U       |
| 920334 | Stephen   | (247) 555-7205 | NULL            | 99N25L1       |
| 929343 | Andrea    | (368) 555-3561 | 7954314541      | 245THL6       |
| 985539 | Lisa      | (118) 555-8106 | NULL            | B3VSJVF       |
+--------+-----------+----------------+-----------------+---------------+

select * from bakery_security_logs
join people on bakery_security_logs.license_plate=people.license_plate
and people.license_plate in
(select license_plate from people where id in
(select person_id from bank_accounts where account_number in
(select account_number from atm_transactions
where day=28 and atm_location='Leggett Street' and transaction_type='withdraw')))
and day=28
and hour=10;
+-----+------+-------+-----+------+--------+----------+---------------+--------+--------+----------------+-----------------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |   id   |  name  |  phone_number  | passport_number | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+--------+--------+----------------+-----------------+---------------+
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       | 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       | 396669 | Iman   | (829) 555-5269 | 7049073643      | L93JTIZ       |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | 514354 | Diana  | (770) 555-1861 | 3592750733      | 322W7JE       |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       | 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       |
+-----+------+-------+-----+------+--------+----------+---------------+--------+--------+----------------+-----------------+---------------+

select * from phone_calls where month=7 and day=28;
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 211 | (336) 555-0077 | (098) 555-1164 | 2024 | 7     | 28  | 318      |
| 212 | (918) 555-5327 | (060) 555-2489 | 2024 | 7     | 28  | 146      |
| 213 | (491) 555-2505 | (478) 555-1565 | 2024 | 7     | 28  | 241      |
| 214 | (996) 555-8899 | (059) 555-4698 | 2024 | 7     | 28  | 142      |
| 215 | (704) 555-5790 | (772) 555-5770 | 2024 | 7     | 28  | 200      |
| 216 | (984) 555-5921 | (618) 555-9856 | 2024 | 7     | 28  | 546      |
| 217 | (579) 555-5030 | (971) 555-6468 | 2024 | 7     | 28  | 421      |
| 218 | (233) 555-0473 | (831) 555-0973 | 2024 | 7     | 28  | 113      |
| 219 | (293) 555-1469 | (749) 555-4874 | 2024 | 7     | 28  | 195      |
| 220 | (450) 555-8297 | (771) 555-7880 | 2024 | 7     | 28  | 298      |
| 221 | (130) 555-0289 | (996) 555-8899 | 2024 | 7     | 28  | 51       |
| 222 | (209) 555-7806 | (693) 555-7986 | 2024 | 7     | 28  | 487      |
| 223 | (918) 555-2946 | (006) 555-0505 | 2024 | 7     | 28  | 359      |
| 224 | (499) 555-9472 | (892) 555-8872 | 2024 | 7     | 28  | 36       |
| 225 | (669) 555-6918 | (914) 555-5994 | 2024 | 7     | 28  | 233      |
| 226 | (547) 555-8781 | (398) 555-1013 | 2024 | 7     | 28  | 272      |
| 227 | (544) 555-8087 | (389) 555-5198 | 2024 | 7     | 28  | 595      |
| 228 | (666) 555-5774 | (125) 555-8030 | 2024 | 7     | 28  | 326      |
| 229 | (047) 555-0577 | (059) 555-4698 | 2024 | 7     | 28  | 379      |
| 230 | (301) 555-4174 | (711) 555-3007 | 2024 | 7     | 28  | 583      |
| 231 | (801) 555-9266 | (984) 555-5921 | 2024 | 7     | 28  | 148      |
| 232 | (971) 555-6468 | (267) 555-2761 | 2024 | 7     | 28  | 149      |
| 233 | (367) 555-5533 | (375) 555-8161 | 2024 | 7     | 28  | 45       |
| 234 | (609) 555-5876 | (389) 555-5198 | 2024 | 7     | 28  | 60       |
| 235 | (357) 555-0246 | (502) 555-6712 | 2024 | 7     | 28  | 305      |
| 236 | (367) 555-5533 | (344) 555-9601 | 2024 | 7     | 28  | 120      |
| 237 | (394) 555-3247 | (035) 555-2997 | 2024 | 7     | 28  | 111      |
| 238 | (839) 555-1757 | (487) 555-5865 | 2024 | 7     | 28  | 278      |
| 239 | (770) 555-1196 | (324) 555-0416 | 2024 | 7     | 28  | 527      |
| 240 | (636) 555-4198 | (670) 555-8598 | 2024 | 7     | 28  | 69       |
| 241 | (068) 555-0183 | (770) 555-1861 | 2024 | 7     | 28  | 371      |
| 242 | (711) 555-3007 | (113) 555-7544 | 2024 | 7     | 28  | 157      |
| 243 | (060) 555-2489 | (204) 555-4136 | 2024 | 7     | 28  | 510      |
| 244 | (704) 555-2131 | (891) 555-5672 | 2024 | 7     | 28  | 103      |
| 245 | (367) 555-5533 | (022) 555-4052 | 2024 | 7     | 28  | 241      |
| 246 | (873) 555-3868 | (047) 555-0577 | 2024 | 7     | 28  | 109      |
| 247 | (867) 555-9103 | (068) 555-0183 | 2024 | 7     | 28  | 116      |
| 248 | (608) 555-9302 | (725) 555-3243 | 2024 | 7     | 28  | 280      |
| 249 | (901) 555-8732 | (491) 555-2505 | 2024 | 7     | 28  | 451      |
| 250 | (478) 555-1565 | (717) 555-1342 | 2024 | 7     | 28  | 573      |
| 251 | (499) 555-9472 | (717) 555-1342 | 2024 | 7     | 28  | 50       |
| 252 | (695) 555-0348 | (338) 555-6650 | 2024 | 7     | 28  | 383      |
| 253 | (696) 555-9195 | (258) 555-5627 | 2024 | 7     | 28  | 525      |
| 254 | (286) 555-6063 | (676) 555-6554 | 2024 | 7     | 28  | 43       |
| 255 | (770) 555-1861 | (725) 555-3243 | 2024 | 7     | 28  | 49       |
| 256 | (711) 555-3007 | (147) 555-6818 | 2024 | 7     | 28  | 358      |
| 257 | (725) 555-4692 | (821) 555-5262 | 2024 | 7     | 28  | 456      |
| 258 | (324) 555-0416 | (452) 555-8550 | 2024 | 7     | 28  | 328      |
| 259 | (234) 555-1294 | (772) 555-5770 | 2024 | 7     | 28  | 573      |
| 260 | (669) 555-6918 | (971) 555-6468 | 2024 | 7     | 28  | 67       |
| 261 | (031) 555-6622 | (910) 555-3251 | 2024 | 7     | 28  | 38       |
| 262 | (342) 555-9260 | (219) 555-0139 | 2024 | 7     | 28  | 404      |
| 263 | (342) 555-9260 | (487) 555-5865 | 2024 | 7     | 28  | 560      |
| 264 | (801) 555-9266 | (608) 555-9302 | 2024 | 7     | 28  | 425      |
| 265 | (398) 555-1013 | (329) 555-5870 | 2024 | 7     | 28  | 237      |
| 266 | (016) 555-9166 | (336) 555-0077 | 2024 | 7     | 28  | 88       |
| 267 | (594) 555-2863 | (491) 555-2505 | 2024 | 7     | 28  | 361      |
| 268 | (122) 555-4581 | (831) 555-0973 | 2024 | 7     | 28  | 491      |
| 269 | (914) 555-5994 | (973) 555-3809 | 2024 | 7     | 28  | 320      |
| 270 | (258) 555-5627 | (695) 555-0348 | 2024 | 7     | 28  | 368      |
| 271 | (751) 555-6567 | (594) 555-6254 | 2024 | 7     | 28  | 61       |
| 272 | (771) 555-7880 | (711) 555-3007 | 2024 | 7     | 28  | 288      |
| 273 | (219) 555-0139 | (867) 555-9103 | 2024 | 7     | 28  | 514      |
| 274 | (676) 555-6554 | (328) 555-9658 | 2024 | 7     | 28  | 153      |
| 275 | (749) 555-4874 | (492) 555-5484 | 2024 | 7     | 28  | 575      |
| 276 | (328) 555-9658 | (775) 555-7584 | 2024 | 7     | 28  | 579      |
| 277 | (219) 555-0139 | (910) 555-3251 | 2024 | 7     | 28  | 121      |
| 278 | (380) 555-4380 | (680) 555-4935 | 2024 | 7     | 28  | 550      |
| 279 | (826) 555-1652 | (066) 555-9701 | 2024 | 7     | 28  | 55       |
| 280 | (594) 555-6254 | (123) 555-5144 | 2024 | 7     | 28  | 346      |
| 281 | (338) 555-6650 | (704) 555-2131 | 2024 | 7     | 28  | 54       |
| 282 | (971) 555-6468 | (258) 555-5627 | 2024 | 7     | 28  | 441      |
| 283 | (730) 555-5115 | (343) 555-0167 | 2024 | 7     | 28  | 101      |
| 284 | (286) 555-6063 | (310) 555-8568 | 2024 | 7     | 28  | 235      |
| 285 | (367) 555-5533 | (704) 555-5790 | 2024 | 7     | 28  | 75       |
| 286 | (041) 555-4011 | (609) 555-5876 | 2024 | 7     | 28  | 565      |
| 287 | (478) 555-1565 | (031) 555-6622 | 2024 | 7     | 28  | 398      |
+-----+----------------+----------------+------+-------+-----+----------+

select * from bakery_security_logs
join people on bakery_security_logs.license_plate=people.license_plate
and people.license_plate in
(select license_plate from people where id in
(select person_id from bank_accounts where account_number in
(select account_number from atm_transactions
where day=28 and atm_location='Leggett Street' and transaction_type='withdraw')))
and bakery_security_logs.day=28
and hour=10 join phone_calls on people.phone_number=phone_calls.caller and phone_calls.month=7 and phone_calls.day=28;
+-----+------+-------+-----+------+--------+----------+---------------+--------+--------+----------------+-----------------+---------------+-----+----------------+----------------+------+-------+-----+----------+
| id  | year | month | day | hour | minute | activity | license_plate |   id   |  name  |  phone_number  | passport_number | license_plate | id  |     caller     |    receiver    | year | month | day | duration |
+-----+------+-------+-----+------+--------+----------+---------------+--------+--------+----------------+-----------------+---------------+-----+----------------+----------------+------+-------+-----+----------+
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 245 | (367) 555-5533 | (022) 555-4052 | 2024 | 7     | 28  | 241      |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 9   | (367) 555-5533 | (113) 555-7544 | 2024 | 7     | 25  | 469      |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 104 | (367) 555-5533 | (238) 555-5554 | 2024 | 7     | 26  | 84       |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 133 | (367) 555-5533 | (286) 555-0131 | 2024 | 7     | 26  | 444      |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 236 | (367) 555-5533 | (344) 555-9601 | 2024 | 7     | 28  | 120      |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 233 | (367) 555-5533 | (375) 555-8161 | 2024 | 7     | 28  | 45       |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 395 | (367) 555-5533 | (455) 555-5315 | 2024 | 7     | 30  | 31       |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 122 | (367) 555-5533 | (660) 555-3095 | 2024 | 7     | 26  | 399      |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 488 | (367) 555-5533 | (696) 555-9195 | 2024 | 7     | 31  | 261      |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 285 | (367) 555-5533 | (704) 555-5790 | 2024 | 7     | 28  | 75       |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 418 | (367) 555-5533 | (841) 555-3728 | 2024 | 7     | 30  | 511      |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       | 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       | 57  | (389) 555-5198 | (368) 555-3561 | 2024 | 7     | 25  | 414      |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       | 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       | 326 | (389) 555-5198 | (609) 555-5876 | 2024 | 7     | 29  | 397      |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       | 396669 | Iman   | (829) 555-5269 | 7049073643      | L93JTIZ       | 442 | (829) 555-5269 | (022) 555-4052 | 2024 | 7     | 30  | 232      |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       | 396669 | Iman   | (829) 555-5269 | 7049073643      | L93JTIZ       | 345 | (829) 555-5269 | (286) 555-0131 | 2024 | 7     | 29  | 337      |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       | 396669 | Iman   | (829) 555-5269 | 7049073643      | L93JTIZ       | 465 | (829) 555-5269 | (367) 555-0409 | 2024 | 7     | 31  | 412      |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | 514354 | Diana  | (770) 555-1861 | 3592750733      | 322W7JE       | 401 | (770) 555-1861 | (123) 555-5144 | 2024 | 7     | 30  | 491      |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | 514354 | Diana  | (770) 555-1861 | 3592750733      | 322W7JE       | 198 | (770) 555-1861 | (680) 555-4935 | 2024 | 7     | 27  | 430      |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | 514354 | Diana  | (770) 555-1861 | 3592750733      | 322W7JE       | 255 | (770) 555-1861 | (725) 555-3243 | 2024 | 7     | 28  | 49       |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | 514354 | Diana  | (770) 555-1861 | 3592750733      | 322W7JE       | 137 | (770) 555-1861 | (770) 555-1196 | 2024 | 7     | 26  | 163      |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       | 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       | 284 | (286) 555-6063 | (310) 555-8568 | 2024 | 7     | 28  | 235      |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       | 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       | 451 | (286) 555-6063 | (344) 555-9601 | 2024 | 7     | 30  | 154      |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       | 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       | 254 | (286) 555-6063 | (676) 555-6554 | 2024 | 7     | 28  | 43       |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       | 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       | 46  | (286) 555-6063 | (789) 555-8833 | 2024 | 7     | 25  | 125      |
+-----+------+-------+-----+------+--------+----------+---------------+--------+--------+----------------+---
select * from bakery_security_logs
join people on bakery_security_logs.license_plate=people.license_plate
and people.license_plate in
(select license_plate from people where id in
(select person_id from bank_accounts where account_number in
(select account_number from atm_transactions
where day=28 and atm_location='Leggett Street' and transaction_type='withdraw')))
and bakery_security_logs.day=28
and hour=10 join phone_calls on people.phone_number=phone_calls.caller and phone_calls.month=7 and phone_calls.day=28;
+-----+------+-------+-----+------+--------+----------+---------------+--------+--------+----------------+-----------------+---------------+-----+----------------+----------------+------+-------+-----+----------+
| id  | year | month | day | hour | minute | activity | license_plate |   id   |  name  |  phone_number  | passport_number | license_plate | id  |     caller     |    receiver    | year | month | day | duration |
+-----+------+-------+-----+------+--------+----------+---------------+--------+--------+----------------+-----------------+---------------+-----+----------------+----------------+------+-------+-----+----------+
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 245 | (367) 555-5533 | (022) 555-4052 | 2024 | 7     | 28  | 241      |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 236 | (367) 555-5533 | (344) 555-9601 | 2024 | 7     | 28  | 120      |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 233 | (367) 555-5533 | (375) 555-8161 | 2024 | 7     | 28  | 45       |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       | 285 | (367) 555-5533 | (704) 555-5790 | 2024 | 7     | 28  | 75       |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | 514354 | Diana  | (770) 555-1861 | 3592750733      | 322W7JE       | 255 | (770) 555-1861 | (725) 555-3243 | 2024 | 7     | 28  | 49       |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       | 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       | 284 | (286) 555-6063 | (310) 555-8568 | 2024 | 7     | 28  | 235      |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       | 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       | 254 | (286) 555-6063 | (676) 555-6554 | 2024 | 7     | 28  | 43       |
+-----+------+-------+-----+------+--------+----------+---------------+--------+--------+----------------+-----------------+---------------+-----+----------------+----------------+------+-------+-----+----------+
Thief is Bruce, Diana or Taylor.
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | 514354 | Diana  | (770) 555-1861 | 3592750733      | 322W7JE       | 255 | (770) 555-1861 | (725) 555-3243 | 2024 | 7     | 28  | 49       |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       | 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       | 284 | (286) 555-6063 | (310) 555-8568 | 2024 | 7     | 28  | 235      |
select passport_number,name from people where name in ('Bruce','Diana', 'Taylor');
+-----------------+--------+
| passport_number |  name  |
+-----------------+--------+
| 1988161715      | Taylor |
| 3592750733      | Diana  |
| 5773159633      | Bruce  |
+-----------------+--------+
select * from passengers where passport_number in (select passport_number from people where name in ('Diana', 'Taylor','Bruce'));
+-----------+-----------------+------+
| flight_id | passport_number | seat |
+-----------+-----------------+------+
| 18        | 3592750733      | 4C   |
| 24        | 3592750733      | 2C   |
| 36        | 5773159633      | 4A   |
| 36        | 1988161715      | 6D   |
| 54        | 3592750733      | 6C   |
+-----------+-----------------+------+
select * from flights join passengers on flights.id=passengers.flight_id and flights.id in (select flight_id from passengers where passport_number in (
select passport_number from people where name in ('Diana', 'Taylor','Bruce'))) and passengers.passport_number in (select passport_number from people where name in ('Diana', 'Taylor','Bruce'));
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute | flight_id | passport_number | seat |
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| 18 | 8                 | 6                      | 2024 | 7     | 29  | 16   | 0      | 18        | 3592750733      | 4C   |
| 24 | 7                 | 8                      | 2024 | 7     | 30  | 16   | 27     | 24        | 3592750733      | 2C   |
| 36 | 8                 | 4                      | 2024 | 7     | 29  | 8    | 20     | 36        | 5773159633      | 4A   |
| 36 | 8                 | 4                      | 2024 | 7     | 29  | 8    | 20     | 36        | 1988161715      | 6D   |
| 54 | 8                 | 5                      | 2024 | 7     | 30  | 10   | 19     | 54        | 3592750733      | 6C   |
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
Thief is Bruce or Taylor
Thief is Bruce as exit timings match more closely.

Duration of phone call is below 60s hence,
select * from people where phone_number='(375) 555-8161';
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |
+--------+-------+----------------+-----------------+---------------+
Accomplice is Robin!

Flight id is 36.
select * from flights where id='36';
+----+-------------------+------------------------+------+-------+-----+------+--------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
+----+-------------------+------------------------+------+-------+-----+------+--------+
| 36 | 8                 | 4                      | 2024 | 7     | 29  | 8    | 20     |
+----+-------------------+------------------------+------+-------+-----+------+--------+
select * from airports where id='4';
+----+--------------+-------------------+---------------+
| id | abbreviation |     full_name     |     city      |
+----+--------------+-------------------+---------------+
| 4  | LGA          | LaGuardia Airport | New York City |
+----+--------------+-------------------+---------------+
New York City!
