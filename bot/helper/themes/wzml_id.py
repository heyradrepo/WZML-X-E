#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Repo'
    ST_BN1_URL = 'https://github.com/heyradrepo/WZML-X-E'
    ST_BN2_NAME = 'Owner'
    ST_BN2_URL = 'https://t.me/xyradelw'
    ST_MSG = '''<i>Hai Aku {context.bot.name} dapat mencerminkan semua tautan|file|torrent Anda ke Google Drive atau cloud rclone mana pun atau ke telegram atau ke server ddl.</i>
<b>Ketik {help_command} untuk mendapat daftar perintahnya</b>'''
    ST_BOTPM = '''<i>Sekarang, aku akan mengirim semuanya di sini. Mulailah ...</i>'''
    ST_UNAUTH = '''<i>Oh sayang sekali, Kamu bukan user yang di izinkan, buat versi mu sendiri</i>'''
    OWN_TOKEN_GENERATE = '''<b>Token sementara ini bukan milikmu!</b>\n\n<i>Buat milikmu sendiri.</i>'''
    USED_TOKEN = '''<b>Token mu sudah terpakai!</b>\n\n<i>Buatlah yang baru.</i>'''
    LOGGED_PASSWORD = '''<b>Bot sudah masuk menggunakan passwd</b>\n\n<i>Tak perlu untuk menyetujuinya lagi.</i>'''
    ACTIVATE_BUTTON = 'Mengaktifkan token mu'
    TOKEN_MSG = '''<b><u>Token Login Sementara Telah Dibuat!</u></b>
<b>Token Sementara:</b> <code>{token}</code>
<b>Berlaku:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Berhasil ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Sudah Masuk Bot!</b>'
    INVALID_PASS = '<b>Password Salah!</b>\n\nMohon masukkan Password yang benar.'
    PASS_LOGGED = '<b>Masuk Bot Secara Permanen Berhasil!</b>'
    LOGIN_USED = '<b>Penggunaan Masuk Bot :</b>\n\n<code>/cmd [password]</code>'

    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Dasar'
    USER_BT = 'Pengguna'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Tutup'
    HELP_HEADER = "㊂ <b><i>Menu Panduan Bantuan!</i></b>\n\n<b>CATATAN: <i>Klik pada CMD apa pun untuk melihat rincian lebih lanjut.</i></b>"


    # async def stats(client, message):
    BOT_STATS = '''⌬ <b><i>STATISTIK KU :</i></b>
┖ <b>Bot Uptime :</b> {bot_uptime}

┎ <b><i>RAM ( MEMORY ) :</i></b>
┃ {ram_bar} {ram}%
┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎ <b><i>SWAP MEMORY :</i></b>
┃ {swap_bar} {swap}%
┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎ <b><i>DISK :</i></b>
┃ {disk_bar} {disk}%
┃ <b>Total Disk Read :</b> {disk_read}
┃ <b>Total Disk Write :</b> {disk_write}
┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = '''⌬ <b><i>OS SYSTEM :</i></b>
┠ <b>OS Uptime :</b> {os_uptime}
┠ <b>OS Version :</b> {os_version}
┖ <b>OS Arch :</b> {os_arch}

⌬ <b><i>JARINGAN STATS :</i></b>
┠ <b>Upload Data:</b> {up_data}
┠ <b>Download Data:</b> {dl_data}
┠ <b>Pkts Terkirim:</b> {pkt_sent}k
┠ <b>Pkts Diterima:</b> {pkt_recv}k
┖ <b>Total I/O Data:</b> {tl_data}

┎ <b>CPU :</b>
┃ {cpu_bar} {cpu}%
┠ <b>CPU Frequency :</b> {cpu_freq}
┠ <b>System Avg Load :</b> {sys_load}
┠ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
┠ <b>Total Core(s) :</b> {total_core}
┖ <b>Usable CPU(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''⌬ <b><i>STATISTIK REPOSITORY :</i></b>
┠ <b>Bot Updated :</b> {last_commit}
┠ <b>Current Version :</b> {bot_version}
┠ <b>Latest Version :</b> {lat_version}
┖ <b>Last ChangeLog :</b> {commit_details}

⌬ <b>REMARKS :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''⌬ <b><i>LIMITASI KU :</i></b>
┠ <b>Direct Limit :</b> {DL} GB
┠ <b>Torrent Limit :</b> {TL} GB
┠ <b>GDrive Limit :</b> {GL} GB
┠ <b>YT-DLP Limit :</b> {YL} GB
┠ <b>Playlist Limit :</b> {PL}
┠ <b>Mega Limit :</b> {ML} GB
┠ <b>Clone Limit :</b> {CL} GB
┖ <b>Leech Limit :</b> {LL} GB

┎ <b>Token Validity :</b> {TV}
┠ <b>User Time Limit :</b> {UTI} / task
┠ <b>User Parallel Tasks :</b> {UT}
┖ <b>Bot Parallel Tasks :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Memulai ulang...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''⌬ <b><i>Mulai ulang berhasil!</i></b>
┠ <b>Tanggal:</b> {date}
┠ <b>Waktu:</b> {time}
┠ <b>ZonaWaktu:</b> {timz}
┖ <b>Versi:</b> {version}'''
    RESTARTED = '''⌬ <b><i>Hai Lagi!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Bagaimana?..</i>'
    PING_VALUE = '<b>Apanya?</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>Tugas Dimulai</i></b>
┠ <b>Mode:</b> {Mode}
┖ <b>Oleh:</b> {Tag}\n\n"""
    LINKS_SOURCE = """➲ <b>Sumber:</b>
┖ <b>Pada :</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "➲ <b><u>Tugas Dimulai :</u></b>\n┃\n┖ <b>tautan:</b> <a href='{msg_link}'>Disini</a>"
    L_LOG_START =           "➲ <b><u>Leech Dimulai :</u></b>\n┃\n┠ <b>pengguna :</b> {mention} ( #ID{uid} )\n┖ <b>Sumber :</b> <a href='{msg_link}'>Disini</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>{Name}</i></b>\n┃\n'
    SIZE =                  '┠ <b>Ukuran: </b>{Size}\n'
    ELAPSE =                '┠ <b>Berlalu: </b>{Time}\n'
    MODE =                  '┠ <b>Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┠ <b>Total File: </b>{Files}\n'
    L_CORRUPTED_FILES =     '┠ <b>File Cacat: </b>{Corrupt}\n'
    L_CC =                  '┖ <b>Oleh: </b>{Tag}\n\n'
    PM_BOT_MSG =            '➲ <b><i>File(s) sudah ku kirim di atas</i></b>'
    L_BOT_MSG =             '➲ <b><i>File(s) sudah ku kirim ke Bot PM (Private)</i></b>'
    L_LL_MSG =              '➲ <b><i>File(s) sudah ku kirim. Akses Melalui Tautan...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '┠ <b>Tipe: </b>{Mimetype}\n'
    M_SUBFOLD =             '┠ <b>SubFolder: </b>{Folder}\n'
    TOTAL_FILES =           '┠ <b>File: </b>{Files}\n'
    RCPATH =                '┠ <b>Jalur: </b><code>{RCpath}</code>\n'
    M_CC =                  '┖ <b>Oleh: </b>{Tag}\n\n'
    M_BOT_MSG =             '➲ <b><i>Link(s) sudah ku kirim ke Bot PM (Private)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b><i>{Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┃ {Bar}'
    PROCESSED =         '\n┠ <b>Processed:</b> {Processed}'
    STATUS =            '\n┠ <b>Status:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ETA:</b> {Eta}'
    SPEED =             '\n┠ <b>Speed:</b> {Speed}'
    ELAPSED =                                     ' | <b>Elapsed:</b> {Elapsed}'
    ENGINE =            '\n┠ <b>Engine:</b> {Engine}'
    STA_MODE =          '\n┠ <b>Mode:</b> {Mode}'
    SEEDERS =           '\n┠ <b>Seeders:</b> {Seeders} | '
    LEECHERS =                                           '<b>Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┠ <b>Size: </b>{Size}'
    SEED_SPEED =     '\n┠ <b>Speed: </b> {Speed} | '
    UPLOADED =                                     '<b>Uploaded: </b> {Upload}'
    RATIO =          '\n┠ <b>Ratio: </b> {Ratio} | '
    TIME =                                         '<b>Time: </b> {Time}'
    SEED_ENGINE =    '\n┠ <b>Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┠ <b>Size: </b>{Size}'
    NON_ENGINE =     '\n┠ <b>Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠ <b>User:</b> <code>{User}</code> | '
    ID =                                                        '<b>ID:</b> <code>{Id}</code>'
    BTSEL =          '\n┠ <b>Select:</b> {Btsel}'
    CANCEL =         '\n┖ {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '⌬ <b><i>Bot Stats</i></b>\n'
    TASKS =  '┠ <b>Tasks:</b> {Tasks}\n'
    BOT_TASKS = '┠ <b>Tasks:</b> {Tasks}/{Ttask} | <b>AVL:</b> {Free}\n'
    Cpu = '┠ <b>CPU:</b> {cpu}% | '
    FREE =                      '<b>F:</b> {free} [{free_p}%]'
    Ram = '\n┠ <b>RAM:</b> {ram}% | '
    uptime =                     '<b>UPTIME:</b> {uptime}'
    DL = '\n┖ <b>DL:</b> {DL}/s | '
    UL =                        '<b>UL:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⫷'
    REFRESH = 'ᴘᴀɢᴇs\n{Page}'
    NEXT = '⫸'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder sudah tersedia di Drive.\nNih {content} list nya:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Menghitung:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '┠ <b>Ukuran: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠ <b>Tipe: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠ <b>SubFolder: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠ <b>File: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┖ <b>Oleh: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Mencari <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Ketemu {NO} hasil untuk <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'Wkwk gk ketemu nih <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>Tidak Ada Unduhan Aktif!</i>
    
⌬ <b><i>Bot Stats</i></b>
┠ <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>User Settings :</u></b>
        
┎<b> Nama :</b> {NAME} ( <code>{ID}</code> )
┠<b> Username :</b> {USERNAME}
┠<b> Telegram DC :</b> {DC}
┖<b> Bahasa :</b> {LANG}

➲ <u><b>Argumen yang tersedia:</b></u>
• <b>-s</b> or <b>-set</b>: Mengatur Langsung melalui Arg'''

    UNIVERSAL = '''㊂ <b><u>Pengaturan Universal : {NAME}</u></b>

┎<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
┠<b> Daily Tasks :</b> <code>{DT}</code> per day
┠<b> Last Bot Used :</b> <code>{LAST_USED}</code>
┠<b> User Session :</b> <code>{USESS}</code>
┠<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┠<b> Save Mode :</b> <code>{SAVE_MODE}</code>
┖<b> User Bot PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>Pengaturan Mirror/Clone : {NAME}</u></b>

┎<b> RClone Config :</b> <i>{RCLONE}</i>
┠<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
┠<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
┠<b> Mirror Remname :</b> <code>{MREMNAME}</code>
┠<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠<b> User TD Mode :</b> <i>{TMODE}</i>
┠<b> Total User TD(s) :</b> <i>{USERTD}</i>
┖<b> Daily Mirror :</b> <code>{DM}</code> per day'''

    LEECH = '''㊂ <b><u>Pengaturan Leech Untuk {NAME}</u></b>

┎<b> Daily Leech : </b><code>{DL}</code> per day
┠<b> Leech Type :</b> <i>{LTYPE}</i>
┠<b> Custom Thumbnail :</b> <i>{THUMB}</i>
┠<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
┠<b> Leech Caption :</b> <code>{LCAPTION}</code>
┠<b> Leech Prefix :</b> <code>{LPREFIX}</code>
┠<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
┠<b> Leech Dumps :</b> <code>{LDUMP}</code>
┖<b> Leech Remname :</b> <code>{LREMNAME}</code>'''
