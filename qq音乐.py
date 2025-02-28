"""
爬虫
作用：采集数据/模拟用户行为
原理： 模拟 浏览器 向 服务器 发送网络请求

1.需求分析
数据在哪里？
#https://ws6.stream.qqmusic.qq.com/RS02062VCVkH3Hm4wk.mp3?guid=3959000840&vkey=D9456A58A54A1781F1146794CAC11E9047EDCF5F239D0819AE2192A1EC1AC7344C9D9E731FA3760BE11E2A5145A80406BAE68E386F25AF37__v2b9ab203&uin=2244378311&fromtag=120052
#{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2244378311,"g_tk_new_20200303":1551440693,"g_tk":1551440693},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["2244378311"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["2244378311"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["001Bbywq2gicae"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"001Bbywq2gicae","songID":102065750}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"102065750","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"003DFRzD192KKD"}},"req_8":{"module":"music.vkey.GetVkey","method":"GetUrl","param":{"guid":"5078374740","songmid":["001Bbywq2gicae"],"songtype":[0],"uin":"2244378311","loginflag":1,"platform":"20","filename":["RS02062VCVkH3Hm4wk.mp3"]}}}:
#https://ws6.stream.qqmusic.qq.com/RS02064dfdIM38rSZY.mp3?guid=1849503000&vkey=9C09537DBF45664E391B996BC8CF7B1CF34B5F9394092A53C18511DCEBAD18F09F0749C9E92755B0F76A6DC51D6C97CD47BE0DE79600E6F0__v2b94c203&uin=2244378311&fromtag=120052
#{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2244378311,"g_tk_new_20200303":1551440693,"g_tk":1551440693},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["2244378311"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["2244378311"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["0039MnYb0qxYhV"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"0039MnYb0qxYhV","songID":97773}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"97773","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"000MkMni19ClKG"}},"req_8":{"module":"music.vkey.GetVkey","method":"GetUrl","param":{"guid":"7038802641","songmid":["0039MnYb0qxYhV"],"songtype":[0],"uin":"2244378311","loginflag":1,"platform":"20","filename":["RS02064dfdIM38rSZY.mp3"]}}}:
2.代码实现
发送请求
获取数据
解析数据
保存数据
"""
import requests #发送请求第三方库 额外安装
headers={
    'cookie':'pgv_pvid=1983789168; fqm_pvqid=6d0e1d6f-74dd-4d47-bfa5-144a3f1ef11a; fqm_sessionid=42e4300b-4543-4d0b-87a5-182525475235; pgv_info=ssid=s8408434106; ts_refer=cn.bing.com/; ts_uid=6303804225; _qpsvr_localtk=0.9808182625773596; RK=VE/d2IG63V; ptcz=6395325c9fa564494e67eae12ffe52350057148c3542338be7ad654678678750; login_type=1; tmeLoginType=2; wxopenid=; psrf_qqaccess_token=D9628A58A67013BFF338C893E6632903; qm_keyst=Q_H_L_63k3N8qhKhOQ11NyrzXMT71XaSdz0Cdso6SZmv069DDD9hxPiANWxS66xSLr2Xj2bHMCDPynM_kDsFdK3A2kRoUmxeP4; music_ignore_pskey=202306271436Hn@vBj; psrf_qqopenid=4C3D8B5CE7EA91A07040612824CF4868; uin=2244378311; psrf_access_token_expiresAt=1741345227; psrf_qqunionid=613BB9C8B9102B7DB31A9BD2C8E743FD; qqmusic_key=Q_H_L_63k3N8qhKhOQ11NyrzXMT71XaSdz0Cdso6SZmv069DDD9hxPiANWxS66xSLr2Xj2bHMCDPynM_kDsFdK3A2kRoUmxeP4; wxunionid=; psrf_qqrefresh_token=A878198DFD997B5ACF4847DDF5CCD0B6; wxrefresh_token=; euin=ow-P7eolNeo5ov**; psrf_musickey_createtime=1740740427; ts_last=y.qq.com/n/ryqq/player'
    'user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
data='{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2244378311,"g_tk_new_20200303":1551440693,"g_tk":1551440693},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["2244378311"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["2244378311"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["001Bbywq2gicae"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"001Bbywq2gicae","songID":102065750}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"102065750","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"003DFRzD192KKD"}},"req_8":{"module":"music.vkey.GetVkey","method":"GetUrl","param":{"guid":"5078374740","songmid":["001Bbywq2gicae"],"songtype":[0],"uin":"2244378311","loginflag":1,"platform":"20","filename":["RS02062VCVkH3Hm4wk.mp3"]}}}:'
url="https://ws6.stream.qqmusic.qq.com/RS02062VCVkH3Hm4wk.mp3?guid=3959000840&vkey=D9456A58A54A1781F1146794CAC11E9047EDCF5F239D0819AE2192A1EC1AC7344C9D9E731FA3760BE11E2A5145A80406BAE68E386F25AF37__v2b9ab203&uin=2244378311&fromtag=120052"
#1.发送请求
response=requests.post(url=url,data=data,headers=headers)
print(response)
#2.获取数据
json_data=response.json()
#3.解析数据
purl=json_data['req_8']['data']['midurlinfo']['0']['purl']
music_url='https://ws6.stream.qqmusic.qq.com/' +purl
music_data = requests.get(music_url).content

