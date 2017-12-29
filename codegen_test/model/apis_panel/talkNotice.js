/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TalkNotice = function () {
    /*
        @params obj 'data params'
            account_ids   'array' 
            talk_id   'string' 
            msg_txt   'string' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/talk_notice",
            method: "POST",
            data: {
                account_ids: obj.account_ids,
                talk_id: obj.talk_id,
                msg_txt: obj.msg_txt
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    TalkNotice: new TalkNotice
};