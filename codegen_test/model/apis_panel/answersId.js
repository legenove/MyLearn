/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AnswersId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            duration   'integer' 
            source   'string' 
            media_id   'ref' 
            
        @success
            status 200    type:object
            status   'string' 
            media_id   'string' 微信media id 三天有效期
            id   'ref' 
            content   'string' 
            voice_url   'string' 保存到七牛的语音地址
            store_type   'string' 
            duration   'integer' 
            date_created   'ref' 
            _voice   'string' 
            voice_id   'string' 
            question_id   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/answers/" + obj.id + "",
            method: "PUT",
            data: {
                duration: obj.duration,
                source: obj.source || "qiniu",
                media_id: obj.media_id
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
    AnswersId: new AnswersId
};