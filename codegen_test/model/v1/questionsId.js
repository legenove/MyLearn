/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsId = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            free_key   'string' free key in query
            rewarder_id   'integer' rewarder id in query
            
        @success
            status 200    type:object
            free_type   'string' 
            library_id   'string' 
            discussions_count   'integer' 
            asker   'ref' 
            respondent   'ref' 
            is_enable_inquiry   'boolean' 
            bonus   'integer' 
            topics   'array' 
            is_free_in_30mins   'boolean' 
            has_discussions   'boolean' 
            is_free   'boolean' 
            has_quota   'boolean' 
            is_limit_free   'boolean' 
            bonuses   'integer' 
            remaining_seconds   'integer' 
            topic_short_title   'string' 
            is_enable_revoke   'boolean' 
            answer   'ref' 
            is_public   'boolean' 
            refuse_reason   'ref' 
            is_tenant_free   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/" + obj.id + "",
            method: "GET",
            data: {
                free_key: obj.free_key,
                rewarder_id: obj.rewarder_id
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
    
    /*
        @params obj 'data params'
            id   'string' question id in path
            duration   'integer' 
            source   'string' 
            media_id   'ref' 
            qiniu_id   'string' 
            
        @success
            status 201    type:object
            likings_count   'integer' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/" + obj.id + "",
            method: "POST",
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
    QuestionsId: new QuestionsId
};