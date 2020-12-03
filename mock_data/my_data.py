# FIELD_LIST and QUICK_LIST are used for the fake 3rd standard library

FIELD_LIST = ['am_pm', 'boolean', 'bothify', 'bs', 'building_number',
              'catch_phrase',
              'century', 'city', 'city_prefix', 'city_suffix', 'color_name',
              'company',
              'company_email', 'company_suffix', 'country', 'country_code',
              'credit_card_expire',
              'credit_card_number', 'credit_card_provider',
              'credit_card_security_code',
              'currency_code', 'date', 'domain_name', 'domain_word', 'ean',
              'ean13', 'ean8',
              'email', 'file_extension', 'file_name', 'file_path', 'first_name',
              'first_name_female', 'first_name_male', 'free_email',
              'free_email_domain',
              'geo_coordinate', 'hex_color', 'image_url', 'internet_explorer',
              'ipv4', 'ipv6',
              'isbn10', 'isbn13', 'iso8601', 'job', 'language_code',
              'last_name',
              'last_name_female', 'last_name_male', 'latitude', 'lexify',
              'linux_platform_token', 'linux_processor', 'locale', 'longitude',
              'mac_address',
              'mac_platform_token', 'mac_processor', 'md5', 'military_apo',
              'military_dpo',
              'military_ship', 'military_state', 'mime_type', 'month',
              'month_name', 'name',
              'name_female', 'name_male', 'null_boolean', 'numerify',
              'password', 'phone_number', 'postalcode', 'postalcode_plus4',
              'postcode',
              'prefix', 'prefix_female', 'prefix_male', 'pybool', 'pydecimal',
              'pyfloat',
              'pyint', 'pystr', 'random_digit', 'random_digit_not_null',
              'random_digit_not_null_or_empty', 'random_digit_or_empty',
              'random_element',
              'random_int', 'random_letter', 'random_number',
              'randomize_nb_elements',
              'safe_color_name', 'safe_email', 'safe_hex_color',
              'secondary_address', 'seed',
              'sentence', 'sha1', 'sha256', 'slug', 'ssn', 'state',
              'state_abbr', 'street_address', 'street_name', 'street_suffix',
              'suffix',
              'suffix_female', 'suffix_male', 'text', 'time',
              'timezone', 'tld', 'unix_time', 'uri', 'uri_extension',
              'uri_page', 'uri_path',
              'url', 'user_agent', 'user_name', 'uuid4',
              'windows_platform_token', 'word',
              'year', 'zipcode', 'zipcode_plus4']

QUICK_LIST = ['random_element', 'random_digit', 'random_digit_not_null',
              'uri_page', 'safe_color_name', 'free_email_domain',
              'military_state',
              'random_int', 'uri_extension', 'state_abbr', 'state', 'pybool',
              'military_ship',
              'pyint', 'tld', 'zipcode', 'random_letter', 'null_boolean',
              'mac_processor',
              'randomize_nb_elements', 'city_prefix', 'linux_processor',
              'company_suffix',
              'postalcode', 'city_suffix', 'unix_time',
              'windows_platform_token', 'boolean',
              'century', 'linux_platform_token', 'word', 'street_suffix',
              'random_digit_not_null_or_empty', 'currency_code', 'hex_color',
              'sha1',
              'credit_card_provider', 'sha256', 'md5', 'country_code',
              'random_digit_or_empty', 'country', 'safe_hex_color', 'timezone',
              'uuid4',
              'geo_coordinate', 'random_number', 'language_code', 'longitude',
              'zipcode_plus4', 'latitude', 'postalcode_plus4', 'mime_type',
              'file_extension',
              'prefix_male', 'job', 'mac_platform_token', 'prefix_female',
              'uri_path',
              'ipv4', 'suffix_female', 'iso8601', 'locale', 'color_name',
              'image_url',
              'internet_explorer', 'file_name', 'ssn', 'bs', 'time', 'numerify',
              'catch_phrase', 'prefix', 'suffix_male', 'lexify', 'suffix',
              'secondary_address', 'date', 'month_name', 'month', 'year',
              'file_path',
              'pyfloat', 'credit_card_security_code', 'pydecimal',
              'mac_address', 'am_pm',
              'ipv6', 'building_number', 'bothify', 'slug', 'ean8',
              'military_apo',
              'military_dpo']

COUNTRY_LIST = ['日本', '美国', '印度', '全球', '澳大利亚', '斯里兰卡', '中国', '印尼', '新加坡', '韩国',
                '香港', '巴基斯坦', '马来西亚', '菲律宾', '泰国', '蒙古', '越南', '孟加拉', '老挝',
                '柬埔寨', '荷兰', '新西兰', '台湾', '瑙鲁', '阿富汗', '巴布亚新几内亚', '德国', '加拿大',
                '不丹', '北马里亚纳群岛', '意大利', '尼泊尔', '萨摩亚', '法国', '摩洛哥', '关岛', '葡萄牙',
                '新喀里多尼亚', '文莱', '法属波利尼西亚', '斐济群岛', '所罗门群岛', '爱尔兰', '瓦努阿图',
                '巴西', '瑞典', '纳米比亚', '南非', '以色列', '肯尼亚', '比利时', '丹麦'
                ]

PROVINCE_LIST = ['北京市', '天津市', '上海市', '重庆市', '河南省', '安徽省', '福建省',
                 '甘肃省', '贵州省', '海南省', '河北省', '黑龙江省', '湖北省', '湖南省',
                 '吉林省', '江苏省', '江西省', '辽宁省', '青海省', '山东省', '山西省',
                 '陕西省', '四川省', '云南省', '浙江省', '台湾省', '广东省',
                 '广西壮族自治区', '内蒙古自治区', '宁夏回族自治区', '西藏藏族自治区',
                 '新疆维吾尔自治区', '香港',
                 '澳门', '台湾']

PROVINCE_CITY_LIST = {
    '北京市': ['北京市'],
    '天津市': ['天津市'],
    '上海市': ['上海市'],
    '重庆市': ['重庆市'],
    '河南省': ['郑州市', '洛阳市', '焦作市', '商丘市', '信阳市', '周口市', '鹤壁市', '安阳市', '濮阳市',
            '驻马店市', '南阳市', '开封市', '漯河市', '许昌市', '新乡市', '济源市', '灵宝市', '偃师市',
            '邓州市', '登封市', '三门峡市', '新郑市', '禹州市', '巩义市', '永城市', '长葛市', '义马市',
            '林州市', '项城市', '汝州市', '荥阳市', '平顶山市', '卫辉市', '辉县市', '舞钢市', '新密市',
            '孟州市', '沁阳市', '郏县'],
    '安徽省': ['合肥市', '亳州市', '芜湖市', '马鞍山市', '池州市', '黄山市', '滁州市', '安庆市', '淮南市',
            '淮北市', '蚌埠市', '宿州市', '宣城市', '六安市', '阜阳市', '铜陵市', '明光市', '天长市',
            '宁国市', '界首市', '桐城市'],
    '福建省': ['福州市', '厦门市', '泉州市', '漳州市', '南平市', '三明市', '龙岩市', '莆田市', '宁德市',
            '建瓯市', '武夷山市', '长乐市', '福清市', '晋江市', '南安市', '福安市', '龙海市', '邵武市',
            '石狮市', '福鼎市', '建阳市', '漳平市', '永安市'],
    '甘肃省': ['兰州市', '白银市', '武威市', '金昌市', '平凉市', '张掖市', '嘉峪关市', '酒泉市', '庆阳市',
            '定西市', '陇南市', '天水市', '玉门市', '临夏市', '合作市', '敦煌市', '甘南州'],
    '贵州省': ['贵阳市', '安顺市', '遵义市', '六盘水市', '兴义市', '都匀市', '凯里市', '毕节市', '清镇市',
            '铜仁市', '赤水市', '仁怀市', '福泉市'],
    '海南省': ['海口市', '三亚市', '万宁市', '文昌市', '儋州市', '琼海市', '东方市', '五指山市'],
    '河北省': ['石家庄市', '保定市', '唐山市', '邯郸市', '邢台市', '沧州市', '衡水市', '廊坊市', '承德市',
            '迁安市', '鹿泉市', '秦皇岛市', '南宫市', '任丘市', '叶城市', '辛集市', '涿州市', '定州市',
            '晋州市', '霸州市', '黄骅市', '遵化市', '张家口市', '沙河市', '三河市', '冀州市', '武安市',
            '河间市', '深州市', '新乐市', '泊头市', '安国市', '双滦区', '高碑店市'],
    '黑龙江省': ['哈尔滨市', '伊春市', '牡丹江市', '大庆市', '鸡西市', '鹤岗市', '绥化市', '齐齐哈尔市', '黑河市',
             '富锦市', '虎林市', '密山市', '佳木斯市', '双鸭山市', '海林市', '铁力市', '北安市', '五大连池市',
             '阿城市', '尚志市', '五常市', '安达市', '七台河市', '绥芬河市', '双城市', '海伦市', '宁安市',
             '讷河市', '穆棱市', '同江市', '肇东市'],
    '湖北省': ['武汉市', '荆门市', '咸宁市', '襄阳市', '荆州市', '黄石市', '宜昌市', '随州市', '鄂州市',
            '孝感市', '黄冈市', '十堰市', '枣阳市', '老河口市', '恩施市', '仙桃市', '天门市', '钟祥市',
            '潜江市', '麻城市', '洪湖市', '汉川市', '赤壁市', '松滋市', '丹江口市', '武穴市', '广水市',
            '石首市', '大冶市', '枝江市', '应城市', '宜城市', '当阳市', '安陆市', '宜都市', '利川市'],
    '湖南省': ['长沙市', '郴州市', '益阳市', '娄底市', '株洲市', '衡阳市', '湘潭市', '岳阳市', '常德市',
            '邵阳市', '永州市', '张家界市', '怀化市', '浏阳市', '醴陵市', '湘乡市', '耒阳市', '沅江市',
            '涟源市', '常宁市', '吉首市', '津市市', '冷水江市', '临湘市', '汨罗市', '武冈市', '韶山市',
            '湘西州'],
    '吉林省': ['长春市', '吉林市', '通化市', '白城市', '四平市', '辽源市', '松原市', '白山市', '集安市',
            '梅河口市', '双辽市', '延吉市', '九台市', '桦甸市', '榆树市', '蛟河市', '磐石市', '大安市',
            '德惠市', '洮南市', '龙井市', '珲春市', '公主岭市', '图们市', '舒兰市', '和龙市', '临江市',
            '敦化市'],
    '江苏省': ['南京市', '无锡市', '常州市', '扬州市', '徐州市', '苏州市', '连云港市', '盐城市', '淮安市',
            '宿迁市', '镇江市', '南通市', '泰州市', '兴化市', '东台市', '常熟市', '江阴市', '张家港市',
            '通州市', '宜兴市', '邳州市', '海门市', '溧阳市', '泰兴市', '如皋市', '昆山市', '启东市',
            '江都市', '丹阳市', '吴江市', '靖江市', '扬中市', '新沂市', '仪征市', '太仓市', '姜堰市',
            '高邮市', '金坛市', '句容市', '灌南县'],
    '江西省': ['南昌市', '赣州市', '上饶市', '宜春市', '景德镇市', '新余市', '九江市', '萍乡市', '抚州市',
            '鹰潭市', '吉安市', '丰城市', '樟树市', '德兴市', '瑞金市', '井冈山市', '高安市', '乐平市',
            '南康市', '贵溪市', '瑞昌市', '东乡县', '广丰县', '信州区', '三清山'],
    '辽宁省': ['沈阳市', '葫芦岛市', '大连市', '盘锦市', '鞍山市', '铁岭市', '本溪市', '丹东市', '抚顺市',
            '锦州市', '辽阳市', '阜新市', '调兵山市', '朝阳市', '海城市', '北票市', '盖州市', '凤城市',
            '庄河市', '凌源市', '开原市', '兴城市', '新民市', '大石桥市', '东港市', '北宁市', '瓦房店市',
            '普兰店市', '凌海市', '灯塔市', '营口市'],
    '青海省': ['西宁市', '格尔木市', '德令哈市'],
    '山东省': ['济南市', '青岛市', '威海市', '潍坊市', '菏泽市', '济宁市', '莱芜市', '东营市', '烟台市',
            '淄博市', '枣庄市', '泰安市', '临沂市', '日照市', '德州市', '聊城市', '滨州市', '乐陵市',
            '兖州市', '诸城市', '邹城市', '滕州市', '肥城市', '新泰市', '胶州市', '胶南市', '即墨市',
            '龙口市', '平度市', '莱西市'],
    '山西省': ['太原市', '大同市', '阳泉市', '长治市', '临汾市', '晋中市', '运城市', '忻州市', '朔州市',
            '吕梁市', '古交市', '高平市', '永济市', '孝义市', '侯马市', '霍州市', '介休市', '河津市',
            '汾阳市', '原平市', '潞城市'],
    '陕西省': ['西安市', '咸阳市', '榆林市', '宝鸡市', '铜川市', '渭南市', '汉中市', '安康市', '商洛市',
            '延安市', '韩城市', '兴平市', '华阴市'],
    '四川省': ['成都市', '广安市', '德阳市', '乐山市', '巴中市', '内江市', '宜宾市', '南充市', '都江堰市',
            '自贡市', '泸州市', '广元市', '达州市', '资阳市', '绵阳市', '眉山市', '遂宁市', '雅安市',
            '阆中市', '攀枝花市', '广汉市', '绵竹市', '万源市', '华蓥市', '江油市', '西昌市', '彭州市',
            '简阳市', '崇州市', '什邡市', '峨眉山市', '邛崃市', '双流县'],
    '云南省': ['昆明市', '玉溪市', '大理市', '曲靖市', '昭通市', '保山市', '丽江市', '临沧市', '楚雄市',
            '开远市', '个旧市', '景洪市', '安宁市', '宣威市'],
    '浙江省': ['杭州市', '宁波市', '绍兴市', '温州市', '台州市', '湖州市', '嘉兴市', '金华市', '舟山市',
            '衢州市', '丽水市', '余姚市', '乐清市', '临海市', '温岭市', '永康市', '瑞安市', '慈溪市',
            '义乌市', '上虞市', '诸暨市', '海宁市', '桐乡市', '兰溪市', '龙泉市', '建德市', '富德市',
            '富阳市', '平湖市', '东阳市', '嵊州市', '奉化市', '临安市', '江山市'],
    '台湾省': ['台北市', '台南市', '台中市', '高雄市', '桃源市'],
    '广东省': ['广州市', '深圳市', '珠海市', '汕头市', '佛山市', '韶关市', '湛江市', '肇庆市', '江门市',
            '茂名市', '惠州市', '梅州市', '汕尾市', '河源市', '阳江市', '清远市', '东莞市', '中山市',
            '潮州市', '揭阳市', '云浮市'],
    '广西壮族自治区': ['南宁市', '贺州市', '玉林市', '桂林市', '柳州市', '梧州市', '北海市', '钦州市', '百色市',
                '防城港市', '贵港市', '河池市', '崇左市', '来宾市', '东兴市', '桂平市', '北流市', '岑溪市',
                '合山市', '凭祥市', '宜州市'],
    '内蒙古自治区': ['呼和浩特市', '呼伦贝尔市', '赤峰市', '扎兰屯市', '鄂尔多斯市', '乌兰察布市', '巴彦淖尔市',
               '二连浩特市', '霍林郭勒市', '包头市', '乌海市', '阿尔山市', '乌兰浩特市', '锡林浩特市', '根河市',
               '满洲里市', '额尔古纳市', '牙克石市', '临河市', '丰镇市', '通辽市'],
    '宁夏回族自治区': ['银川市', '固原市', '石嘴山市', '青铜峡市', '中卫市', '吴忠市', '灵武市'],
    '西藏藏族自治区': ['拉萨市', '日喀则市'],
    '新疆维吾尔自治区': ['乌鲁木齐市', '石河子市', '喀什市', '阿勒泰市', '阜康市', '库尔勒市', '阿克苏市', '阿拉尔市',
                 '哈密市', '克拉玛依市', '昌吉市', '奎屯市', '米泉市', '和田市'],
    '香港': ['香港'],
    '澳门': ['澳门'],
    '台湾': ['台北', '新北', '台中', '台南', '高雄', '桃园', '嘉义', '基隆']
}

GENDERS = ['男', '女', '未知']

APP_LIST = ['虎扑体育', 'QQ输入法', '腾讯新闻', 'POLARIS Office 5', 'Max+', '铁路12306',
             'QQ音乐', '天天快报', '掌上英雄联盟', '多玩约战', '携程旅行', '来疯直播', '榴莲', 'QQ浏览器',
             '百度糯米商家', '哔哩哔哩动画', '华数TV', '京东金融', 'QQ安全中心', '快手看片', '陌陌', '美团外卖',
             '小恩爱', '作业帮', '内涵段子', '铁友火车票12306抢票', 'TripAdvisor猫途鹰', '凤凰FM',
             '黄油相机', '优酷', '土豆视频', '手机百度', '苏宁易购', '瓜子二手车', '冲浪快讯', '腾讯动漫',
             '贴吧极速版', '万年历', '腾讯课堂', '大智慧', 'QQ空间', '搜狗地图', '股市教练', '广发手机证券-旧版',
             '二手车之家', 'QQ阅读', '阅读王', '天气通', '书旗小说', '360优化大师']

APP_LIST_FULL = ['虎扑体育', 'QQ输入法', '腾讯新闻', 'POLARIS Office 5', 'Max+', '铁路12306',
                 'QQ音乐', '天天快报', '掌上英雄联盟', '多玩约战', '携程旅行', '来疯直播', '榴莲',
                 'QQ浏览器',
                 '百度糯米商家', '哔哩哔哩动画', '华数TV', '京东金融', 'QQ安全中心', '快手看片', '陌陌',
                 '美团外卖',
                 '小恩爱', '作业帮', '内涵段子', '铁友火车票12306抢票', 'TripAdvisor猫途鹰', '凤凰FM',
                 '黄油相机', '优酷', '土豆视频', '手机百度', '苏宁易购', '瓜子二手车', '冲浪快讯', '腾讯动漫',
                 '贴吧极速版', '万年历', '腾讯课堂', '大智慧', 'QQ空间', '搜狗地图', '股市教练',
                 '广发手机证券-旧版',
                 '二手车之家', 'QQ阅读', '阅读王', '天气通', '书旗小说', '360优化大师', '平安好医生',
                 '中关村在线',
                 '玩图', '上网导航', '映客直播', '一账通', '91桌面', '网易有道词典', '一点资讯', '动动',
                 '腾讯视频',
                 '凤凰视频', '搜狗阅读', '授权管理', '懂球帝', '分期乐', '导航犬', '芒果TV', '快手',
                 '阿里星球',
                 '追书神器', '飞凡', '百姓网', '招才猫直聘', '搜狐视频', '广东移动', '百度视频', 'QQ邮箱',
                 '2345天气王', '网址导航', '黄历天气', '新浪新闻', '乐视体育', '58帮帮', '元贝驾考',
                 '58违章查询',
                 '阅读星', '折800', 'WiFi万能钥匙', '新浪财经', '小米应用商店', '唱吧', '360手机急救箱',
                 '链家',
                 '南方航空', '喜马拉雅FM', '京东阅读', '途虎养车', '一起作业学生', '掌上营业厅', '小红书',
                 '大众点评',
                 '美团', '华为商城', 'in', '快牙', '乐词-新东方背单词', '嘀嗒拼车', '堆糖', '飞常准',
                 '网易公开课',
                 '移动图书馆', '139邮箱', '电话手表', '豆瓣电影', '领英', '二维码扫描-查真伪', '坏男孩',
                 '汽车报价',
                 '并读', '美人相机', '简拼', '和讯财经', '天涯社区', '九游', '饿了么', '米家', '驴妈妈旅游',
                 '车主无忧', '微博头条', '安居客', '闲鱼', 'PP助手', '猎豹安全大师', 'MM商场', '全民TV',
                 '咪咕音乐', '当当', '小影', '手机京东', '娃娃', '金十数据', '央视影音', '石榴直播', '最右',
                 '宜搜搜索', '微云', '妈妈网-怀孕育儿亲子辣妈孕期', '腾讯体育', '神州专车', '网易云课堂', '丁香园',
                 '齐齐互动视频', '当当读书', '华住', '当乐', '世纪佳缘', '广西移动', '网易邮箱大师',
                 '51信用卡管家',
                 '航旅纵横', '净网大师', '潮自拍', '孕育管家-备孕孕妇孕期经期助手', '汽车超人-洗车养车专家', '卷皮',
                 '百合婚恋', '美柚', '买车达人-在线全城砍价', '双色球', '微爱', '安卓市场',
                 '百度手机助手（原91助手）',
                 '铃音', '360智能摄像机', '精品街9块9', '漫画人', 'QQ游戏', '迅雷', 'LOFTER',
                 '益盟操盘手经典版', '单身交友', '钱盾', '搜狗手机助手', '每日新款', '人人-高校美女直播', '储蓄罐',
                 '美丽约', '小米视频', '我要自学网', '趣店', '英语趣配音', '网易考拉海购', '宝宝知道',
                 '手机助手',
                 '流量宝', '违章查询助手', '儿歌多多', '东方财富网', '应用中心', 'e代驾', '快看免费小说',
                 'Feel',
                 'KK', '纳米盒', '风水罗盘买房租房指南针', '禾连健康', '柚子街', '新浪博客', '酷狗铃声',
                 '10000社区', '搜狗浏览器', '啪啪音乐圈', '花椒直播', '魔力相册', '天翼云', '铃声多多',
                 'DJ多多',
                 '1药网', '汽车之家', '中国蓝TV', '钱大掌柜', '点心省电', '平安WiFi', 'QQ', '一折特卖',
                 'YY', '116114', '拼多多', '蜻蜓FM', '足记', '驾考宝典', '卷皮折扣', '交汇点新闻',
                 '考研帮',
                 '逗拍', '澎湃新闻', '微会', '应用宝', '钓鱼人', '应用汇', '鲸鱼宝理财', '随手记',
                 '掌阅iReader', '快看漫画', 'Boss直聘', '返还购', '北京移动', '知米背单词',
                 '考拉FM电台',
                 '疯狂造人-备孕怀孕', '卡牛信用卡管家', '小蚁摄像机', '安徽移动', '软件商店', '360手机助手',
                 '酷我听书FM电台', '用药助手', '360影视大全', '快的打车', '360免费WiFi', 'ES 任务管理器',
                 'ES文件浏览器', 'OPPO社区', '有缘网', '漫漫漫画', '妈妈社区', '去哪儿旅行',
                 '贵州移动10086',
                 '宜搜小说', '音悦台', '电视家2.0', '太平洋电脑网', '免费电子书', '购物大厅', '懒人听书',
                 '快快查汉语字典', 'WiFi 连网神器', 'LBE加速大师', '米折', '箩筐', '速算盒子', 'nice',
                 '易班',
                 '美咖相机', '有信电话', '56视频', '天天P图', '直播吧', '漫画岛', '随e行WLAN',
                 '12306买火车票', '美甲帮', 'LT来电闪光', '中华万年历日历', '最美天气', '好大夫在线',
                 '皮皮影视',
                 '全国违章查询', '买车宝典', '我查查', '今日头条', '暴风影音', '春雨计步器', '沪江小D词典',
                 '网易新闻',
                 '孕期伴侣', '中国天气通', '360省电王', '360游戏大厅', '微信电话本', '万能遥控', '荔枝FM',
                 '相机360', '优理宝', '快看影视']

GENDERS_LIST = ['男', '女', '未知']

order_status_list = ['用户拒收', '未付款的订单', '用户取消', '待发货', '配送中', '确认收货']
pay_level_list = ['低级', '中级', '高级', '钻石']
pay_from_list = ['支付宝', '微信', '银联', '其他']
is_appraise_list = ['未点评', '已点评']
appraise_level_list = ['一星', '两星', '三星', '四星', '五星']
deliver_companies = ['中通', '圆通', '顺丰', 'EMS', '韵达', '申通', '百世汇通', '其他']

