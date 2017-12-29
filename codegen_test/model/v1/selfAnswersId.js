/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var SelfAnswersId = function () {
    /*
        @params obj 'data params'
            id   'string' answer id in path
            duration   'integer' 
            source   'string' 
            media_id   'ref' 
            qiniu_id   'string' 
            
        @success
            status 200    type:object
            status   'string' 
            is_reanswered   'boolean' 
            voice_obj   'ref' 
            free_key   'string' 
            date_updated   'ref' 
            is_free   'boolean' 
            content   'string' 
            duration   'integer' 
            voice   'string' 
            id   'ref' 
            voice_id   'string' 
            question_id   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/self/answers/" + obj.id + "",
            method: "PUT",
            data: {
                duration: obj.duration,
                source: obj.source || "weixin",
                media_id: obj.media_id,
                qiniu_id: obj.qiniu_id
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
    SelfAnswersId: new SelfAnswersId
};