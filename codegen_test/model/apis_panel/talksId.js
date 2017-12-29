/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TalksId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:object
            introduction   'string' 
            answers_count   'integer' 
            guide   'string' 
            description   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/talks/" + obj.id + "",
            method: "GET",
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
            id   'string' string id in path
            content   'string' 
            account_id   'ref' 
            is_sticky   'boolean' 
            introduction   'string' 
            order_score   'integer' 
            is_active   'boolean' 
            _image   'string' 
            share_description   'string' 
            share_title   'string' 
            is_hot   'boolean' 
            guide   'string' 
            description   'string' 
            
        @success
            status 200    type:object
            content   'ref' 
            listenings_count   'integer' 
            operator_id   'ref' 
            account_id   'ref' 
            is_sticky   'boolean' 
            date_updated   'ref' 
            is_active   'boolean' 
            order_score   'integer' 
            _image   'string' 
            share_description   'string' 
            share_title   'string' 
            date_created   'ref' 
            is_hot   'boolean' 
            type   'string' 
            id   'ref' 
            answers_count   'integer' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/talks/" + obj.id + "",
            method: "PUT",
            data: {
                content: obj.content,
                account_id: obj.account_id,
                is_sticky: obj.is_sticky,
                introduction: obj.introduction,
                order_score: obj.order_score,
                is_active: obj.is_active,
                _image: obj._image,
                share_description: obj.share_description,
                share_title: obj.share_title,
                is_hot: obj.is_hot,
                guide: obj.guide,
                description: obj.description
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
    TalksId: new TalksId
};